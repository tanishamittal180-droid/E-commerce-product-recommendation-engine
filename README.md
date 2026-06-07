# E-Commerce Product Recommendation Engine

## Overview

The E-Commerce Product Recommendation Engine is an AI-powered web application built using Python, Streamlit, SQLite, and Machine Learning techniques. The system provides personalized product recommendations, user authentication, shopping cart functionality, wishlist management, order tracking, product reviews, inventory management, and an admin dashboard.

This project simulates a real-world e-commerce platform similar to Amazon or Flipkart while demonstrating recommendation system concepts and full-stack application development.

## Features

### User Features

* User Registration and Login
* User Profile Management
* Product Search and Filtering
* Shopping Cart
* Wishlist
* Buy Now Functionality
* Order History
* Product Reviews and Ratings
* Recently Viewed Products

### Recommendation Features

* Content-Based Recommendation System
* TF-IDF Vectorization
* Cosine Similarity Matching
* Similar Product Suggestions
* Category-Based Recommendations
* Customers Also Bought Recommendations

### Admin Features

* Admin Login
* Product Management
* Add New Products
* Delete Products
* Inventory Management
* User Management
* Sales Dashboard
* Revenue Analytics
* Product Image Upload

### Analytics

* Product Statistics
* Category Distribution
* Sales Reports
* Revenue Visualization
* Data Export Functionality


## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* SQLite

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Cosine Similarity

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly


## Project Structure

project/

├── app.py

├── assets/

│   └── products/

├── data/

│   ├── products.csv

│   ├── interactions.csv

│   └── users.csv

├── database/

│   ├── db.py

│   └── schema.py

├── pages/

│   ├── auth.py

│   ├── home.py

│   ├── products.py

│   ├── cart.py

│   ├── wishlist.py

│   ├── recommendations.py

│   ├── profile.py

│   ├── orders.py

│   ├── product_reviews.py

│   ├── analytics.py

│   ├── admin_login.py

│   ├── admin_dashboard.py

│   ├── inventory.py

│   ├── product_management.py

│   └── sales_dashboard.py

├── src/

│   ├── recommender.py

│   └── history.py

├── requirements.txt

└── README.rd


## Installation

### Clone Repository

git clone <repository-url>

cd ecommerce-product-recommendation-engine

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt


## Database Setup

Run the schema file:

python database/schema.py

This will create:

* users
* cart
* wishlist
* orders
* reviews
* inventory

tables automatically.

## Running the Application

streamlit run app.py

Application will be available at:

http://localhost:8501


## Recommendation System Workflow

1. Load Product Dataset
2. Extract Product Descriptions
3. Apply TF-IDF Vectorization
4. Calculate Cosine Similarity
5. Find Similar Products
6. Generate Personalized Recommendations
7. Display Recommendations to Users


## Future Enhancements

* Deep Learning Recommendations
* Collaborative Filtering
* Real Payment Gateway Integration
* Product Editing Module
* Email Notifications
* JWT Authentication
* Cloud Deployment
* Docker Support
* Password Encryption using Bcrypt
* REST API Integration

## screenshots
<img width="1352" height="687" alt="Screenshot 2026-06-07 144136" src="https://github.com/user-attachments/assets/01de4e9e-24c7-420c-87cf-fe3cec5c36ad" />
<img width="1365" height="674" alt="Screenshot 2026-06-07 144222" src="https://github.com/user-attachments/assets/35320611-5fab-4191-8ef1-68a690bed4b0" />
<img width="1361" height="656" alt="Screenshot 2026-06-07 144233" src="https://github.com/user-attachments/assets/1fbefab1-e2ab-4522-831b-f5090398e6a0" />
<img width="1358" height="666" alt="Screenshot 2026-06-07 144244" src="https://github.com/user-attachments/assets/6eee41a7-f034-48be-a749-696ac2ddc8e3" />
<img width="1364" height="661" alt="Screenshot 2026-06-07 144323" src="https://github.com/user-attachments/assets/ed9f13b7-8788-48f3-ae37-5d39e1045688" />
<img width="1366" height="707" alt="Screenshot 2026-06-07 144501" src="https://github.com/user-attachments/assets/0e7ada7d-11ea-44d3-80ce-a4767275063d" />
<img width="1360" height="671" alt="Screenshot 2026-06-07 144423" src="https://github.com/user-attachments/assets/336b4439-9c31-40bd-830f-631cbfb33f05" />
<img width="1366" height="675" alt="Screenshot 2026-06-07 144444" src="https://github.com/user-attachments/assets/7741e805-7ef6-4862-9880-0421b3ca08f4" />
<img width="1365" height="689" alt="Screenshot 2026-06-07 144522" src="https://github.com/user-attachments/assets/feda45f8-680c-41fb-88a2-18f12f115f95" />
<img width="1366" height="668" alt="Screenshot 2026-06-07 144604" src="https://github.com/user-attachments/assets/235341f5-0be7-40c3-b716-659875194c43" />

## Learning Outcomes

This project demonstrates:

* Recommendation Systems
* Machine Learning Fundamentals
* Database Management
* Full Stack Development
* User Authentication
* Data Analytics
* Streamlit Application Development
* Software Engineering Practices


## Author

Developed as an Industry-Oriented Machine Learning and Full Stack Development Project.

## License

This project is intended for educational and learning purposes.
