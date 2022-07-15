import profile
from fastapi import FastAPI, Depends, HTTPException
from .auth import AuthHandler
from .schemas import AuthDetails, Auth


app = FastAPI()


auth_handler = AuthHandler()
users = []

@app.post('/register', status_code=201)
def register(auth_details: AuthDetails):
    if any(x['email'] == auth_details.email for x in users):
        raise HTTPException(status_code=400, detail='Email is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'first_name': auth_details.first_name,
        'last_name': auth_details.last_name,
        'profile': auth_details.profile,
        'email': auth_details.email,
        'password': hashed_password
            
    })
    return {"User Register successfully"}


@app.post('/login')
def login(auth: Auth):
    user = None
    for x in users:
        if x['email'] == auth.email:
            user = x
            break
    
    if (user is None) or (not auth_handler.verify_password(auth.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid Email and/or password')
    token = auth_handler.encode_token(user['email'])
    return { 'token': token }


# @app.get('/unprotected')
# def unprotected():
#     return { 'hello': 'world' }


@app.get('/authorized_user')
def protected(email=Depends(auth_handler.auth_wrapper)):
    return { 'name': email }