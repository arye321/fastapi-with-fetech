# uvicorn main:app --reload
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse 
"""
Trying fastapi_login package :)
"""
from datetime import timedelta
from fastapi.requests import Request
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from starlette.responses import Response
SECRET = 'f691b8d9c25109a525637a43d9b6399565cd7437f0c8bdb8'

app = FastAPI()
fake_db = {'asdf': {'password': 'asdf'}}

manager = LoginManager(SECRET, token_url='/auth/token', use_cookie=True)
manager.useRequest(app)

@manager.user_loader()
def load_user(email: str):  # could also be an asynchronous function
    user = fake_db.get(email)
    return user


@app.get('/showcase')
def showcase(request: Request):
    # None if unauthorized
    user = request.state.user
    return f"{user}"

@app.post('/auth/token')
def login(response: Response,data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = load_user(email)  # we are using the same function to retrieve the user
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif password != user['password']:
        raise InvalidCredentialsException
    short_token = manager.create_access_token(
        data=dict(sub=email), expires=timedelta(days=1)
    )
    manager.set_cookie(response, short_token)
    return {'access_token': short_token, 'token_type': 'bearer'}

@app.get('/protected')
def protected_route(user=Depends(manager)):
    return f"user: {user}"


@app.get("/")
async def read_root() -> dict:
    # return {"message": "Welcome to your todo list."}
    return FileResponse('static/index.html')

