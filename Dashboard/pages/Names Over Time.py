import streamlit as st
import plotly.express as px

from Home import df


def get_top_n_names_by_year(df, year, gender, n, by='Number'):
    df = df[(df['Year'] == year) & (df['Gender'] == gender)]
    df = df.sort_values(by=by, ascending=False)
    return list(df['Name'].head(n))


def plot_names_over_time(df, names, gender, view_type):
    view_type = 'Number' if view_type == '# of Babies' else 'Proportion'
    df = df[(df['Name'].isin(names)) & (df['Gender'] == gender)]
    df = df.sort_values(by='Year', ascending=True)
    fig = px.line(
        data_frame=df,
        x='Year',
        y=view_type,
        color='Name'
    )

    fmt = '.1%' if view_type == 'Proportion by Year' else ',.0f'
    fig.update_layout(yaxis=dict(tickformat=fmt))

    return fig


col1, col2, col3 = st.columns([2, 4, 4])

with col1:
    gender = st.radio(
        label='Select a Gender: ',
        options=['M', 'F'],
    )

with col2:
    year = st.slider(
        label='Select a Year: ',
        min_value=1880,
        max_value=2021,
        value=2021
    )

with col3:
    num_names = st.slider(
        label='Select # of Names: ',
        min_value=1,
        max_value=15,
        value=5
    )

view_type = st.radio(
    label='Select a view:',
    options=['# of Babies', '% of Babies']
)

names = get_top_n_names_by_year(df, year, gender, num_names)
top_names_fig = plot_names_over_time(df, names, gender, view_type)
st.plotly_chart(top_names_fig)
