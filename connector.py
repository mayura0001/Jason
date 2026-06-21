'''
pip install "fastapi[standard]" python-dotenv requests   --> install deps
uvicorn connector:app --reload    --> run command, connector = filename, app = FastAPI() var
(Press CTRL+C to quit)            --> stop the server
http://127.0.0.1:8000/docs#        --> FastAPI auto docs, test the API here

FastAPI - RestAPI python framework, communicates between server(backend) and frontend
Uvicorn - Python ASGI server that actually runs FastAPI

GET : Read  --> Read data from the server
POST : Create --> Create new data on the server
PUT : Update --> Update existing data on the server
DELETE : Delete --> Delete data from the server
'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from main import send_message, chat_history

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


# A bare `user_input: str` param (like before) gets read as a query param.
# Your frontend sends JSON {"message": "..."} as the body, so we need a
# Pydantic model - FastAPI then knows to parse it from the request body.
class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"message": "Server is up and running!"}


@app.post("/chat")
def chat(req: ChatRequest):
    return send_message(req.message)


@app.get("/history")
def get_history():
    return {"history": chat_history}