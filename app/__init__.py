from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

from . import routes

def main():
    run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()