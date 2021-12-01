from pydantic import BaseModel



class ProductSchema(BaseModel):
    description: str
    price: float
    technical_details: str
    image: str
    visible: bool 

class ShowProductSchema(ProductSchema):
    id: str
    class Config:
        orm_mode = True
