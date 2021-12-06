from pydantic import BaseModel




class CustomerSchema(BaseModel):
   firstName: str
   lastName: str
   phoneNumber: str
   genre: str
   documentId: str
   birthDate: str


class ShowCustomerSchema(CustomerSchema):
    id: str
    class Config:
        orm_mode = True