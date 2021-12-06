from datetime import datetime
from pydantic import BaseModel
from enum import Enum 


class CouponType(str, Enum):
    VALUE = 'value'
    PERCENTAGE = 'percentantage'
class CouponSchema(BaseModel):
   
    code: str
    expire_at: datetime
    limit: int
    type: CouponType
    value: float

