from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def server():
    return {"message" : "Server is running"}
