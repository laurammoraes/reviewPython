from pydantic import BaseModel
from app.api.customer.schemas import ShowCustomerSchema





class AdressesSchema(BaseModel):
    adress: str
    city: str
    state: str
    number: str
    zipcode: str
    neighbourhood: str
    primary: int
    customer_id: int

class ShowAdressesSchema(AdressesSchema):
    id: str
    customer: ShowCustomerSchema
    class Config:
        orm_mode = True