import random

import pandas as pd


def customers_also_bought():

    products = pd.read_csv(
        "data/products.csv"
    )

    return products.sample(4)