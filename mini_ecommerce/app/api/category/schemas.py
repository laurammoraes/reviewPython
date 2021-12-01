from pydantic import BaseModel



class CategorySchema(BaseModel):
    name: str
   

class ShowCategorySchema(CategorySchema):
    id: str
    class Config:
        orm_mode = True