from pydantic import BaseModel



class SupplierSchema(BaseModel):
   name: str
class ShowSupplierSchema(SupplierSchema):
    id: str
    class Config:
        orm_mode = True

