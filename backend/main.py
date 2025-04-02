from fastapi import FastAPI

app = FastAPI(title="PostOrbit")

@app.get("/")
async def home():
    return "works!"

