#uvicorn main:app --reload
import os
from datetime import timedelta
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
import motor.motor_asyncio
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from starlette.responses import Response

load_dotenv()

SECRET = os.getenv("FASTAPI_LOGIN_SECRET")

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client.testTrufa



app = FastAPI()

origins = ["https://arye321-fastapi-with-fetech-q7w55v47hxv9x-3000.githubpreview.dev"]

manager = LoginManager(SECRET, token_url='/auth/token', use_cookie=True)

manager.useRequest(app)

@manager.user_loader()
async def load_user(email: str):  # could also be an asynchronous function
    user = await db["users"].find_one({"email": email.get("email")})

    return user


app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)


@app.get('/showcase')
def showcase(request: Request):
    # None if unauthorized
    user = request.state.user
    return f"{user.get('email')}"

@app.get("/")
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.post("/singin")
async def singin(response: Response,email:dict) :

    if (user := await db["users"].find_one({"email": email.get("email")})) is not None:
        short_token = manager.create_access_token(
            data=dict(sub=email), expires=timedelta(days=1)
        )
        manager.set_cookie(response, short_token)
        return f"""{email.get("email")} exists"""
    print(email.get("email"))
    insert = await db["users"].insert_one({"email": email.get("email") })
    print(insert)
    return f"created {email}"


@app.post("/test")
async def test(email: dict):
    return f"lol {email}"


@app.post("/cookie")
def create_cookie(response: Response,username: dict):
    print(username)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value",samesite='none')
    return {"message": "Come to the dark side, we have cookies"}
