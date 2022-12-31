import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.markdown("# Main page")


@st.cache
def load_data():
    return pd.read_csv('names.csv')


df = load_data()
df['Proportion'] / df.groupby(['Year', 'Gender'])['Num'].transform('sum')
