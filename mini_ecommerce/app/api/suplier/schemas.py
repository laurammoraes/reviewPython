from pydantic import BaseModel



class SuplierSchema(BaseModel):
   name: str
class ShowSuplierSchema(SuplierSchema):
    id: str
    class Config:
        orm_mode = True