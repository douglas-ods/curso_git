import pandas as pd
import numpy as np
import streamlit as st 
import matplotlib
from src.extraction import load_data

st.set_page_config(layout="wide")

df_raw = load_data()
st.dataframe(df_raw)

if __name__=="__main__":
    load_data()