from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Define a GET(read) endpoint at the root URL
def greet():
    return {"Hello": "World!"} # Return a JSON response with a greeting message