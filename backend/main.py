from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


todos = [
    {
        "id": "1",
        "item": "Read a book."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    }
]


app = FastAPI()

origins = [
    "https://arye321-fastapi-with-fetech-x5jggrp5cp4v4-5501.githubpreview.dev"
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




@app.post("/test")
async def test(username: dict):
    
    return f"lol {username}"