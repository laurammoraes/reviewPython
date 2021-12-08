from pydantic import BaseModel



class AdminSchema(BaseModel):
    displayname:str
    email: str
    role: str
    password: str
   

class ShowAdminSchema(AdminSchema):
    id: str
    class Config:
        orm_mode = True