from bs4 import BeautifulSoup
import favicon

def url_to_title(url: str):
    if url.endswith('/'):
        url = url[:-1]
    if url.startswith('http'):
        url = url.replace('http://', '')
    if url.startswith('https'):
        url = url.replace('https://', '')
    return url
    

def get_website_title(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('title')

    if title is None:
        return url_to_title(url)
    
    return title.text

def get_favicon_url(url):
    icons = favicon.get(url)
    if len(icons) == 0:
        return 'http://localhost:8080/default_icon'
    return icons[0].url

def get_website_description(tags_metadata):
    description = ''
    for meta in tags_metadata:
        if meta.has_attr('name'):
            meta_name = meta.attrs['name']
            if meta_name == 'description':
                description = meta.attrs['content']
    
    return description