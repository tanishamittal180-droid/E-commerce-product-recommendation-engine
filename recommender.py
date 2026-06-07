import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RecommendationEngine:

    def __init__(self):

        self.products = pd.read_csv(
            "data/products.csv"
        )

        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.products["description"]
        )

        self.similarity_matrix = cosine_similarity(
            self.tfidf_matrix
        )

    def get_similar_products(
            self,
            product_id,
            top_n=5):

        idx = self.products[
            self.products["product_id"] == product_id
        ].index[0]

        scores = list(
            enumerate(
                self.similarity_matrix[idx]
            )
        )

        scores = sorted(
            scores,
            key=lambda x: x[1],
            reverse=True
        )

        recommendations = []

        for i in scores[1:top_n+1]:

            product = self.products.iloc[i[0]]

            recommendations.append({
                "id": product["product_id"],
                "name": product["name"],
                "score": round(i[1] * 100, 2)
            })

        return recommendations


def recommend_products(
        category,
        top_n=5):

    products = pd.read_csv(
        "data/products.csv"
    )

    products = products[
        products["category"] == category
    ]

    products = products.sort_values(
        by="rating",
        ascending=False
    )

    return products.head(top_n)