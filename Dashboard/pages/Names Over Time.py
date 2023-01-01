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
    fmt = '.1%' if view_type == 'Proportion' else ',.1f'

    fig = px.line(
        data_frame=df,
        x='Year',
        y=view_type,
        color='Name',
        labels={
            'Number': '# of children born',
            'Proportion': '% of children born'
        }
    )

    fig.update_layout(yaxis=dict(tickformat=fmt))

    return fig


st.sidebar.header('Names over time')
st.sidebar.caption('Modify your selections below')
gender = st.sidebar.radio(
    label='Select a Gender: ',
    options=['Male', 'Female'],
)

year = st.sidebar.slider(
    label='Select a Year: ',
    min_value=1880,
    max_value=2021,
    value=2021
)

num_names = st.sidebar.slider(
    label='Select # of Names: ',
    min_value=1,
    max_value=15,
    value=5
)

st.title('Visualizing names over time')
st.text('This page highlights the top names of a given year and visualizes them over time.')

view_type = st.radio(
    label='Select a view:',
    options=['# of Babies', '% of Babies'],
    horizontal=True
)

names = get_top_n_names_by_year(df, year, gender, num_names)
top_names_fig = plot_names_over_time(df, names, gender, view_type)

config = {'displayModeBar': False}
st.plotly_chart(top_names_fig, config=config)

with st.expander("How to use this information"):
    st.write("""
    Use the slicers in the sidebar and the toggle above the chart to modify your selections. \n
    Selecting a _Year_, _Gender_, and _Number of Names_ will find the top names of that selection. The graph will then show how these names have changed in popularity over time.
    """)
