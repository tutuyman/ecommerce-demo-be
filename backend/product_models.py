from sqlalchemy import Column, Integer, String, Float, DECIMAL
from database import Base

class Product(Base):
    __tablename__ = "customer_view_Table"  # Nama tabel sesuai dengan deskripsi database Anda

    StockCode = Column(String(255), primary_key=True, index=True)
    Description = Column(String(255), nullable=True)
    Brand = Column(String(255), nullable=True)
    Category = Column(String(255), nullable=True)
    Quantity = Column(Integer, nullable=True)
    RemainingShelfLife = Column(String(255), nullable=True)
    SLED_BBD = Column(String(255), nullable=True)
    RetailPrice = Column(Integer, key="Retail Price" ,nullable=True)
    ProductCost = Column(Integer,key="Product Cost", nullable=True)
    CustomerID = Column(Integer, nullable=True)
    OfferPrice = Column(Integer, key="Offer Price", nullable=True)
    Disc_From_Retail = Column(DECIMAL(10, 2), nullable=True)  # Pastikan 'key' cocok dengan kolom database

