from pydantic import BaseModel

# from app.api.




class CustomerSchema(BaseModel):
   firstName: str
   lastName: str
   phoneNumber: str
   genre: str
   documentId: str
   birthDate: str
   user_id: str


    


class ShowCustomerSchema(CustomerSchema):
    id: str
    # user: ShowUserSchema
    class Config:
        orm_mode = True