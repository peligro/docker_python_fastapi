from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def ejemplo():
    return "hola mundo"