from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
from utils import news_model2schema

import json

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/news/{news_id}")
def get_one_news(news_id: int, db: Session = Depends(get_db)):
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return schemas.IResponse(code=200, data=news_model2schema(db_news))

@app.get("/news/batch/{date}")
def get_batch_news(date: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_news = crud.get_news_by_date(db, date=date, skip=skip, limit=limit)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return schemas.IResponse(code=200, data=[news_model2schema(news) for news in db_news])

@app.post("/news/{news_id}")
def update_news(news_id: int, news: schemas.NewsCreate, db: Session = Depends(get_db)):
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    crud.update_news(db, news_id=news_id, news=news)
    return schemas.IResponse(code=200, msg="Update success", data=None)