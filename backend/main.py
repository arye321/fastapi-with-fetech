# uvicorn main:app --reload
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse 

app = FastAPI()
# app.mount("/", StaticFiles(directory="static",html = True), name="static")

# origins = [
#     "https://arye321-fastapi-with-fetech-x5jggrp5cp4v4-5501.githubpreview.dev"
# ]


# app.add_middleware(
#         CORSMiddleware,
#         allow_origins=origins,
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"]
# )

@app.post("/cookie")
def create_cookie(response: Response,username: dict):
    print(username)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}

@app.get("/")
async def read_root() -> dict:
    # return {"message": "Welcome to your todo list."}
    return FileResponse('static/index.html')




@app.post("/test")
async def test(username: dict):
    return f"lol {username}"