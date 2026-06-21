'''
pip install "fastapi[standard]".  --> install fastapi and its dependencies
uvicorn connector:app --reload    --> run command, _____:app //blanch should be the file meme
(Press CTRL+C to quit)            --> stop the server
http://127.0.0.1:8000/docs#        --> Fast API Terminal to test the API

FastAPI - is a RestAPI python based api help to communicate between server(backend) and the frontend
Uvicorn - Python Server

GET : Read  --> Read data from the server
POST : Create --> Create new data on the server
PUT : Update --> Update existing data on the server
DELETE : Delete --> Delete data from the server

'''

from main import send
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Server is up and running!"}

@app.post("/chat")
def chat(user_input: str):
    return {"message": send(user_input)}