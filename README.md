// Versions used for this project

python version = 3.14.6
node version = v24.14.1


// Setup

Install Python and Node first

python3 -m venv .venv
source .venv/bin/activate

pip install requests python-dotenv fastapi "uvicorn[standard]"


// API Setup Guide

1. Go to https://openrouter.ai/workspaces/default/keys and Create a unlimited Key
2. create .env file 
3. OPENROUTER_API_KEY={your api key}