import pandas as pd


def recommend_category(
        category):

    products = pd.read_csv(
        "data/products.csv"
    )

    products = products[
        products["category"]
        == category
    ]

    products = products.sort_values(
        by="rating",
        ascending=False
    )

    return products.head(5)