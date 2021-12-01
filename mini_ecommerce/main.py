from fastapi import FastAPI
from app.api.router import router
from app.models.models import Base
from app.db.db import engine

Base.metadata.create_all(engine)


app = FastAPI()

app.include_router(router)

#python3 -m venv venv
#source venv/bin/activate
#pip install uvicorn
# uvicorn main:app