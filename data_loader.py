# src/data_loader.py

import pandas as pd

def load_products():

    return pd.read_csv(
        "data/products.csv"
    )

def load_users():

    return pd.read_csv(
        "data/users.csv"
    )

def load_interactions():

    return pd.read_csv(
        "data/interactions.csv"
    )