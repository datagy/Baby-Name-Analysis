import streamlit as st
import pandas as pd
import plotly.express as px

from Home import df


def get_unique_names(gender, df=df):
    return df[df['Gender'] == gender]['Name'].sort_values().unique().tolist()


def get_name_metrics(df, gender, name):
    max_year = df['Year'].max()
    prev_year = max_year - 1

    def get_name_rank(df, gender, name, year):
        df = df[
            (df['Gender'] == gender) & (df['Year'] == year)]\
            .sort_values(by='Number', ascending=False)

        df['Rank'] = df['Number'].rank(ascending=False, method='min')
        df = df.set_index('Name')

        try:
            return (int(df.loc[name, 'Rank']), len(df))
        except KeyError:
            return (None, None)

    return get_name_rank(df, gender, name, max_year), get_name_rank(df, gender, name, prev_year)


def generate_metrics_card(metrics):
    curr, prev = metrics
    curr_metric, curr_length = curr
    prev_metric, prev_length = prev

    if all([curr_metric, prev_metric]):
        return st.metric(
            label='Name Ranking',
            value=curr_metric,
            # value=f'{curr_metric} (out of {curr_length:,})',
            delta=curr_metric-prev_metric,
            delta_color='inverse',
            help=f'out of {curr_length} names'
        )

    elif not curr:
        return st.metric(
            label='Name Ranking',
            value='Not ranked'
        )

    elif not prev:
        return st.metric(
            label='Name Ranking',
            value=f'{curr}'
        )


def name_popularity_over_time(name, gender, view_type, df=df):
    filtered = df[(df['Name'] == name) & (df['Gender'] == gender)]
    filtered = filtered.sort_values(by='Year', ascending=True)

    view_type = 'Number' if view_type == '# of Babies' else 'Proportion'
    fmt = ',.1%' if view_type == 'Proportion' else ',.0f'

    fig = px.line(
        data_frame=filtered,
        x='Year',
        y=view_type,
        labels={
            'Number': '# of children born',
            'Proportion': '% of children born'
        }
    )

    fig.layout.yaxis.tickformat = fmt

    return fig


st.title("Get information about a name")
col1, col2 = st.columns(2)

with col1:
    gender = st.radio('Select a gender:', options=[
                      'Male', 'Female'], horizontal=True)

with col2:
    name = st.selectbox(label='Select a Name: ',
                        options=get_unique_names(gender))


metrics = get_name_metrics(df, gender, name)
generate_metrics_card(metrics)

view_type = st.radio(
    label='Select a view:',
    options=['# of Babies', '% of Babies'],
    horizontal=True
)

st.plotly_chart(name_popularity_over_time(name, gender, view_type))
