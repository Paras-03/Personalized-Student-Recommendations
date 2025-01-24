from plots import plot_Score, plot_Accuracy, plot_Mistake_Count, plot_Time
import pickle
from fastapi import FastAPI
import uvicorn
import pandas as pd
from pydantic import BaseModel


app = FastAPI()

with open("./Model/model.pkl", "rb") as file:
    similarity = pickle.load(file)

data = pd.read_csv("./Data/final.csv")

class Recomend(BaseModel):
    title: str
    score: int

@app.get("/ping")
async def ping():
    return "Hi..."

@app.post("/recommend")
def recommend(input: Recomend):
    title = input.title
    score = input.score
    idx = data[(data["title"] == title) & (data["score"] == score)].index[0]
    ans = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])[
        1:3
    ]
    results = set()
    for row in ans:
        results.add(data["topic"][row[0]].strip())
    return results


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port="8000")