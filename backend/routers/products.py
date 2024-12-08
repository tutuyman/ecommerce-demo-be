from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
# from database import get_db
# from product_models import Product  # Import dari product_models.py
from schemas import ProductResponse

#punya gcp
from database import get_data_from_bigquery
from dotenv import load_dotenv
import os

# Load variabel lingkungan dari .env
load_dotenv()


router = APIRouter()

# @router.get("/products", response_model=list[ProductResponse])
# def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     products = db.query(Product).offset(skip).limit(limit).all()
#     #Tetapkan nilai default untuk DiscFromRetail jika NULL

#     for product in products:
#         if product.Disc_From_Retail is None:
#             product.Disc_From_Retail = 0.00

#     if not products:
#         raise HTTPException(status_code=404, detail="No products found")
#     return products



# Ambil konfigurasi dari .env
PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")
TABLE_NAME = os.getenv("TABLE_NAME")


@router.get("/products", response_model=list[ProductResponse])
def get_products(skip: int = Query(0), limit: int = Query(10)):
    query = f"""
    SELECT StockCode, NamaItem, Category, Quantity, RemainingShelfLife, RetailPrice, CustomerID, OfferPrice, DiscFromRetail
    FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_NAME}`
    LIMIT {limit} OFFSET {skip}
    """
    data = get_data_from_bigquery(query)
    if not data:
        raise HTTPException(status_code=404, detail="No products found")
    return [ProductResponse(**item) for item in data]