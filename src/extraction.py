import pandas as pd

def load_data():
    df = pd.read_csv("data/processed/bikes_completed.csv")
    return df 