# main.py

from src.data_loader import *
from src.recommender import *

products = load_products()

users = load_users()

interactions = load_interactions()

while True:

    print("\n===== PRODUCT RECOMMENDER =====")

    print("1. Recommend Products")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        uid = input(
            "Enter User ID: "
        )

        recs = recommend_products(
            uid,
            products,
            interactions
        )

        print("\nRecommendations:\n")

        for product in recs:

            print(
                product["name"],
                "| Rating:",
                product["rating"]
            )

    elif choice == "2":

        break