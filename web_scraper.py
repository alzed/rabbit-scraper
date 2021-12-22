import requests
from bs4 import BeautifulSoup
import re

def sanitize(item, filter):
    if item.has_attr('name') and (not filter or re.match(filter+':.*', item.get('name'))):
        return item.attrs
        
    if item.has_attr('property') and (not filter or re.match(filter+':.*', item.get('property'))):
        return item.attrs
    

def get_meta_data(url, type):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    resp = html.find_all('meta')
    return list(filter(lambda a: a is not None, [sanitize(r, type) for r in resp]))

