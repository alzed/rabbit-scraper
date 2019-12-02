import requests
from bs4 import BeautifulSoup

def sanitize(item):
    if item.get('name'):
        return {
            "name": item.get('name'),
            "content": item.get('content')
        }

def get_html(url, tag):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html5lib')
    res = html.find_all(tag)
    if tag == 'meta':
        return list(filter(lambda a: a is not None, map(sanitize , res)))
    return [r.get_text() for r in res] 
