from fastapi import FastAPI
from web_scraper import get_html

rabbit_scraper = FastAPI()

@rabbit_scraper.get("/v1/api")
def root(url: str, tag: str = 'meta'):
    data = get_html(url, tag)
    return data
