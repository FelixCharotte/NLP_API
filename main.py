from fastapi import FastAPI

app = FastAPI()


@app.get("/{value}")
async def root(value):
    value = math.sqrt(value)
    return {"message": "Hello World",{value}}