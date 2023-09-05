from sqlalchemy.orm import Session

import models, schemas

def get_news(db: Session, news_id: int):
    return db.query(models.News).filter(models.News.id == news_id).first()

def get_news_by_date(db: Session, date: int, skip:int = 0, limit: int = 100):
    return db.query(models.News).filter(models.News.date == date).offset(skip).limit(limit).all()

def update_news(db: Session, news_id: int, news: schemas.NewsCreate):
    # 从数据库中获取要更新的新闻
    db_news = db.query(models.News).filter(models.News.id == news_id).first()

    if db_news:
        # 更新新闻的属性
        db_news.news_title = news.news_title
        db_news.news_keywords = news.news_keywords
        db_news.news_intro = news.news_intro
        db_news.news_method = news.news_method
        db_news.news_conclusion = news.news_conclusion
        db_news.news_rephrase = news.news_rephrase
        db_news.news_related_work = news.news_related_work

        # 提交事务以保存更改
        db.commit()

        # 刷新并返回更新后的新闻
        db.refresh(db_news)
        return db_news