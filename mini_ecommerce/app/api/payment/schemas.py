from pydantic import BaseModel



class PaymentSchema(BaseModel):
    name: str
    enabled: int

class ShowPaymentSchema(PaymentSchema):
    id: str
    class Config:
        orm_mode = True