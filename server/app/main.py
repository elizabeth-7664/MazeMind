from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os 
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="MazeMind API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],   #TODO: restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return { "message": "Welcome to MazeMind API" }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

