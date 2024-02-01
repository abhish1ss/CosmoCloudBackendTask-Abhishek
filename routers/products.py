# routers/products.py
from fastapi import APIRouter, HTTPException, Query
from pymongo import MongoClient
from datetime import datetime

router = APIRouter()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]
product_collection = db["products"]

# ... (the rest of the product-related code from main.py)
