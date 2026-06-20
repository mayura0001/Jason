'''
pip install "fastapi[standard]".  --> install fastapi and its dependencies
uvicorn connector:app --reload    --> run command, _____:app //blanch should be the file meme
(Press CTRL+C to quit)            --> stop the server
http://127.0.0.1:8000/docs        --> Fast API Terminal to test the API

FastAPI - is a RestAPI python based api help to communicate between server(backend) and the frontend
Uvicorn - Python Server

GET : Read  --> Read data from the server
POST : Create --> Create new data on the server
PUT : Update --> Update existing data on the server
DELETE : Delete --> Delete data from the server

'''


from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Define a GET(read) endpoint at the root URL
def greet():
    return {"Hello": "World!"} # Return a JSON response with a greeting message