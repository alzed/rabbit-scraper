import requests
from bs4 import BeautifulSoup
import re

def sanitize(item, filter):
    if item.has_attr('name') and (not filter or re.match(filter+':.*', item.get('name'))):
        return item.attrs
        
    if item.has_attr('property') and (not filter or re.match(filter+':.*', item.get('property'))):
        return item.attrs
    

def get_html(url):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    return html

def get_metadata(url, type):
    html = get_html(url)
    data = html.find_all('meta')
    return list(filter(lambda a: a is not None, [sanitize(d, type) for d in data]))

