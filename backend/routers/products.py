from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from product_models import Product  # Import dari product_models.py
from schemas import ProductResponse

router = APIRouter()

# @router.get("/products", response_model=list[ProductResponse])
# def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     products = db.query(Product).offset(skip).limit(limit).all()
#     if not products:
#         raise HTTPException(status_code=404, detail="No products found")
#     return products

@router.get("/products", response_model=list[ProductResponse])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()

    # Tetapkan nilai default untuk DiscFromRetail jika NULL
    for product in products:
        if product.Disc_From_Retail is None:
            product.Disc_From_Retail = 0.00

    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products
