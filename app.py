import pandas as pd
import numpy as np
import streamlit as st 

def load_data():
    df = pd.read_csv("data/processed/bikes_completed.csv")
    return df 

if __name__=="__main__":
    load_data()