from fastapi import FastAPI
from pydantic import BaseModel
from utils import normalize_text
from model import load_model, load_dictionary
from read_config import read_env_var


app = FastAPI()
language = read_env_var("language")
model = load_model(language)
dictionary = load_dictionary(language)
print(f"Loading model with language {language}")


class Sentiment(BaseModel):
    phrase: str


class Result(BaseModel):
    phrase: str
    language: str
    positive: float
    negative: float


@app.put("/api/analize", response_model=Result)
def get_users(sentiment: Sentiment):
    result = model.predict([normalize_text(dictionary, sentiment.phrase)])
    return Result(phrase=sentiment.phrase, positive=result[0][1], negative=result[0][0], language=language)