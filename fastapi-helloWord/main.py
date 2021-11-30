from fastapi import FastApi, status 
from typing import List
from fastapi.exceptions import HTTPException


app = FastApi()

@app.get('/')
def index():

    return { 'msg': 'hello '}

