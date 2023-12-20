import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go 
from streamlit_lottie import st_lottie

# Page Config
st.set_page_config(
    page_title="Home", 
    page_icon=":bar_chart:", 
    layout="wide",
    initial_sidebar_state="expanded")

# Load Data
@st.cache_data(ttl=6000)
def load_data(url):
    data = pd.read_csv(url)
    return data

# Set Title and Subtitle
st.title("Machine Learning Practice")
st.subheader("A collection of various machine learning applications and models")
st.divider()

# Set Sidebar
with st.sidebar:
    st.write("By Jose Mari Angelo Abeleda")