import models, schemas
import json

def news_model2schema(db_news: models.News):
    newsEntity = schemas.NewsEntity(
        id=db_news.id,
        date=db_news.date,
        pdf=db_news.pdf,
        title=db_news.title,
        doi=db_news.doi,
        abstract=db_news.abstract,
        url=db_news.url,
        publisher=db_news.publisher,
        journal=db_news.journal,
        year=db_news.year,
        license=json.loads(db_news.license),
        subject=json.loads(db_news.subject),
        category=db_news.category,
        authors=json.loads(db_news.authors),
        figures=json.loads(db_news.figures),
        news_title=db_news.news_title,
        news_keywords=db_news.news_keywords,
        news_intro=db_news.news_intro,
        news_method=db_news.news_method,
        news_conclusion=db_news.news_conclusion,
        news_rephrase=db_news.news_rephrase,
        news_related_work=db_news.news_related_work,
        news_figures=db_news.news_figures,
        news_references=json.loads(db_news.news_references)
    )
    return newsEntity