#dipake buat sql lokal, tapi nariknya ada bugg jadi yang ketarik dikit

# from sqlalchemy import Column, Integer, String, Float, DECIMAL
# from database import Base

# class Product(Base):
#     __tablename__ = "customer_view_Table"  # Nama tabel sesuai dengan deskripsi database Anda

#     StockCode = Column(String(255), primary_key=True, index=True)
#     NamaItem = Column(String(255), nullable=True)  # Tambahkan NamaItem
#     Category = Column(String(255), nullable=True)
#     Quantity = Column(Integer, nullable=True)
#     RemainingShelfLife = Column(String(255), nullable=True)
#     RetailPrice = Column(Integer, nullable=True)
#     CustomerId = Column(Integer, nullable=True)  # Tambahkan CustomerID
#     OfferPrice = Column(Integer, nullable=True)
#     DiscFromRetail = Column(DECIMAL(10, 2), nullable=True)
