from fastapi import FastAPI
from web_scraper import get_meta_data

rabbit_scraper = FastAPI()

@rabbit_scraper.get("/v1/api/meta")
def meta(url: str, type: str = ''):
    data = get_meta_data(url, type)
    return data

