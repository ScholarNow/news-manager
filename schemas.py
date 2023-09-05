from pydantic import BaseModel
from typing import List, Any

class AuthorEntity(BaseModel):
    name: str
    org: List[list]
    sequence: str

class FigureEntity(BaseModel):
    capture: str
    text: List[str]
    oss_name: str

class NewsBase(BaseModel):
    date: int = ""
    pdf: str = ""
    title: str = ""
    doi: str = ""
    abstract: str = ""
    url: str = ""
    publisher: str = ""
    journal: str = ""
    year: str = ""
    license: List[str] = []
    subject: List[str] = []
    category: str = ""
    authors: List[AuthorEntity] = []
    figures: List[FigureEntity] = []
    news_title: str = ""
    news_keywords: str = ""
    news_intro: str = ""
    news_method: str = ""
    news_conclusion: str = ""
    news_rephrase: str = ""
    news_related_work: str = ""
    news_figures: str = ""
    news_references: List[str] = []

class NewsCreate(NewsBase):
    news_title: str
    news_keywords: str
    news_intro: str
    news_method: str
    news_conclusion: str
    news_rephrase: str
    news_related_work: str 
    pass

class NewsEntity(NewsBase):
    id: int

    class Config:
        orm_mode = True

class NewsLogBase(BaseModel):
    id: int
    details: str

class NewsLogCreate(NewsLogBase):
    pass

class NewsLogEntity(NewsLogBase):
    class Config:
        orm_mode = True

class IResponse(BaseModel):
    code: int = 200
    msg: str = ""
    data: Any

