
python version = 3.14.6

python3 -m venv .venv
source .venv/bin/activate

pip install requests
pip install dotenv

pip install "fastapi[standard]"
uvicorn connector:app --reload 
(Press CTRL+C to quit)

FastAPI - is a RestAPI python based api help to communicate between server(backend) and the frontend
Uvicorn - Python Server

GET : Read
POST : Create
PUT : Update
DELETE : Delete