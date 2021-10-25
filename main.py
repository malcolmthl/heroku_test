from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def print_f():
    return {"MESSAGE" :"HELLO MAL HERE PASS HEROKU"}