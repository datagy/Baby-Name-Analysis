import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.sidebar.markdown("# Home")
st.markdown("# Social Security Baby Names Analysis")
st.markdown('## Overview')
st.write("""
This analysis provides an overview of the data provide by the [SSA on baby names over time](https://www.ssa.gov/oact/babynames/limits.html).
The analyses provided here hope to provide a new angle on name popularity over time. 
""")

st.markdown("## What's included?")
st.markdown("### Name Popularity Over Time")
st.markdown('Provides a high-level overview of the top `n` names of a given year for either gender. The popularity of these names is tracked over time, shown as counts and proportions of all names.')
st.markdown("### Name Information")
st.markdown('Provides a high-level overview of a particular name, showing popularity over time and some other interesting highlights.')


@st.cache
def load_data():
    df = pd.read_csv('names.csv')
    df['Proportion'] = df['Number'] / \
        df.groupby(['Year', 'Gender'])['Number'].transform('sum')

    df['Gender'] = df['Gender'].map({'M': 'Male', 'F': 'Female'})
    df['Starting Letter'] = df['Name'].str[0]
    return df


df = load_data()
