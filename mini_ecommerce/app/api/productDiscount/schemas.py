from pydantic import BaseModel
from enum import Enum 



class DiscountMode(str, Enum):
    VALUE = 'value'
    PERCENTAGE = 'percentantage'

class ProductDiscountSchema(BaseModel):
    mode: DiscountMode
    value: float
    payment_method_id: int
    product_id: int

