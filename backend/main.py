#uvicorn main:app --reload

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

origins = [
    "https://arye321-fastapi-with-fetech-q7w55v47hxv9x-3000.githubpreview.dev"
]


app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)


@app.get("/")
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.post("/singin")
async def singin(email:dict) :
    print(email)
    return f"asdf {email}"


@app.post("/test")
async def test(email: dict):
    return f"lol {email}"


@app.post("/cookie")
def create_cookie(response: Response,username: dict):
    print(username)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value",samesite='none')
    return {"message": "Come to the dark side, we have cookies"}
