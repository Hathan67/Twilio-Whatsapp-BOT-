from pydantic import BaseModel

class Product(BaseModel):
    Order_id: int
    product: str
    amount: int