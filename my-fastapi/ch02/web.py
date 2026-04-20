from typing import List

from fastapi import FastAPI
from ch02.model import Champion
import data as data
app = FastAPI()

@app.get("/champions")
def get_champions() -> List[Champion]:
    return data.get_champion()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("web:app", host="0.0.0.0", port=8000)