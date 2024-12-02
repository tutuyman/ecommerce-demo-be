from typing import Optional
from pydantic import BaseModel

class ProductResponse(BaseModel):
    StockCode: str
    Description: str
    Brand: str
    Category: str
    Quantity: int
    RemainingShelfLife: str
    RetailPrice: int
    OfferPrice: int
    Disc_From_Retail: Optional[float]  # Ubah menjadi opsional

    class Config:
        orm_mode = True


