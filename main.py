from fastapi import FastAPI

app = FastAPI(
    title = "Hello API",
    summary = "This is a simple FastAPI application",
    version = "1.0.0",
    )

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/square/{number}")
def square(number: int):
    return {
         "result": number ** 2
        }
