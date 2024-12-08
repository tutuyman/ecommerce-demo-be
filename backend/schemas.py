from typing import Optional
from pydantic import BaseModel

# class ProductResponse(BaseModel):
#     StockCode: str
#     Description: str
#     Brand: str
#     Category: str
#     Quantity: int
#     RemainingShelfLife: str
#     RetailPrice: int
#     OfferPrice: int
#     Disc_From_Retail: Optional[float]  # Ubah menjadi opsional

#     class Config:
#         orm_mode = True


class ProductResponse(BaseModel):
    StockCode: str
    NamaItem: str  # Tambahkan NamaItem sesuai query
    Category: str
    Quantity: int
    RemainingShelfLife: str
    RetailPrice: int
    CustomerId: Optional[int] = None  # Tambahkan CustomerID sesuai query
    OfferPrice: Optional[int]  # Pastikan opsional jika NULL di database
    DiscFromRetail: Optional[float]  # Pastikan opsional jika NULL di database

    class Config:
        orm_mode = True


