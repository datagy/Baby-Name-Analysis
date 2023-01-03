import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

from Home import df


def calculate_unique_names_by_year(df=df):
    summary = pd.pivot_table(
        data=df,
        index=['Year', 'Gender'],
        values='Name',
        aggfunc='count'
    ).reset_index()

    fig = px.line(
        data_frame=summary,
        x='Year',
        y='Name',
        color='Gender',
        title='# of unique names by year'
    )

    return fig


def get_unique_names_by_starting_letter(year, df=df):
    summary = pd.pivot_table(
        data=df[df['Year'] == year],
        index=['Starting Letter', 'Gender'],
        values='Name',
        aggfunc='count',
    ).reset_index()

    summary['Name'] = np.where(
        summary['Gender'] == 'Female',
        summary['Name'] * -1,
        summary['Name']
    )

    summary = summary.sort_values(by='Starting Letter', ascending=False)

    return px.bar(
        data_frame=summary,
        y='Starting Letter',
        x='Name',
        color='Gender',
        labels={
            'Name': '# of Unique Names'
        },
        height=600,
        title='# of Unique Names by Starting Letter'
    )


st.header('Under construction')

st.plotly_chart(calculate_unique_names_by_year())
year = st.slider(
    label='Select a year:',
    min_value=df['Year'].min(),
    max_value=df['Year'].max(),
    value=2021
)
st.plotly_chart(get_unique_names_by_starting_letter(year))
