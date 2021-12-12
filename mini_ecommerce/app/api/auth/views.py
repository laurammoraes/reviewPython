from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter()

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login' )    

@router.get('/')
def index( token: str = Depends(oauth_scheme)):
    pass 

@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    pass
