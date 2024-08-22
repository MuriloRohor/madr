from fastapi import FastAPI

from madr.schemas import Message

app = FastAPI()


@app.get("/", response_model=Message)
def root():
    return {"message": "Olá Mundo"}
