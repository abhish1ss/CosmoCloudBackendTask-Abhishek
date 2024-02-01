# models.py
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    quantity: int

class OrderItem(BaseModel):
    productId: str
    boughtQuantity: int
    totalAmount: float

class UserAddress(BaseModel):
    city: str
    country: str
    zipCode: str

class Order(BaseModel):
    items: list[OrderItem]
    userAddress: UserAddress
