import requests
from bs4 import BeautifulSoup
import re

def sanitize(item, filter):
    if item.has_attr('name'):
        if not filter:
            return {
                "name": item.get('name'),
                "content": item.get('content')
            }
        if re.match(filter+':.*', item.get('name')):
            return {
                "name": item.get('name'),
                "content": item.get('content')
            } 
        
    if item.has_attr('property'):
        if not filter:
            return {
                "property": item.get('property'),
                "content": item.get('content')
            }
        if re.match(filter+':.*', item.get('property')):
            return {
                "property": item.get('property'),
                "content": item.get('content')
            }
    

def get_meta_data(url, type):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    resp = html.find_all('meta')
    return list(filter(lambda a: a is not None, [sanitize(r, type) for r in resp]))
