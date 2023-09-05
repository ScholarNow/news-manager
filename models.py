# The models(orm) aim to interact with database.

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Integer, index=True)
    pdf = Column(String(255), index=True)
    title = Column(String(255))
    doi = Column(String(255))
    abstract = Column(Text)
    url = Column(String(255))
    publisher = Column(String(255))
    journal = Column(String(255))
    year = Column(String(255), index=True)
    license = Column(Text)
    subject = Column(Text)
    category = Column(String(255))
    authors = Column(Text)
    figures = Column(Text)
    news_title = Column(Text)
    news_keywords = Column(Text)
    news_intro = Column(Text)
    news_method = Column(Text)
    news_conclusion = Column(Text)
    news_rephrase = Column(Text)
    news_related_work = Column(Text)
    news_figures = Column(Text)
    news_references = Column(Text)

class NewsLogs(Base):
    __tablename__ = "news_logs"

    id = Column(Integer, ForeignKey("news.id"), primary_key=True, index=True)
    details = Column(Text)
