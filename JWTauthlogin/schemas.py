import email
from pydantic import BaseModel


class AuthDetails(BaseModel):
    first_name: str
    last_name: str
    profile:str
    email: str
    password: str
    
    
class Auth(BaseModel):
    email: str
    password: str
    
    
    
    