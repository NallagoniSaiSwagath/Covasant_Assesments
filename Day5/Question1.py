import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import os
from urllib.parse import urljoin
import re

def clean_url_filename(url):
    url1 = url.replace('http://', '').replace('https://', '')[:100]
    cleaned = re.sub(r'[^\w\-_\.]', '_', url1)
    return cleaned

def fetch_page(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return url, response.text
    except:
        return url, None

def get_links(base_url, html_content):
    if not html_content:
        return []
    soup = BeautifulSoup(html_content, 'html.parser')
    return [urljoin(base_url, anchor['href']) for anchor in soup.find_all('a', href=True) if urljoin(base_url, anchor['href']).startswith(('http://', 'https://'))]

def save_site(start_url, max_workers=5):  
    os.makedirs('pages', exist_ok=True)
    _, content = fetch_page(start_url)
    if not content:
        return
    links = get_links(start_url, content)
    with open(os.path.join('pages', clean_url_filename(start_url) + '.html'), 'w') as file:
        file.write(content)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for url, content in executor.map(fetch_page, links):
            if content:
                with open(os.path.join('pages', clean_url_filename(url) + '.html'), 'w') as file:
                    file.write(content)

if __name__ == "__main__":
    save_site("https://example.com")  
