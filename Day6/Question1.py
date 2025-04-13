import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import re

def clean_url_filename(url):
    return re.sub(r'[^\w\-_\.]', '_', url.replace('http://', '').replace('https://', '')[:100])

async def fetch_page(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            response.raise_for_status()
            return url, await response.text()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return url, None

def get_links(base_url, html_content):
    if not html_content:
        return []
    soup = BeautifulSoup(html_content, 'html.parser')
    return [
        urljoin(base_url, a['href'])
        for a in soup.find_all('a', href=True)
        if urljoin(base_url, a['href']).startswith(('http://', 'https://'))
    ]

async def save_site(start_url):
    os.makedirs('pages1', exist_ok=True)

    async with aiohttp.ClientSession() as session:
        # Download the main page
        url, content = await fetch_page(session, start_url)
        if content:
            with open(os.path.join('pages1', clean_url_filename(url) + '.html'), 'w', encoding='utf-8') as f:
                f.write(content)

            # Extract links and download them concurrently
            links = get_links(start_url, content)
            tasks = [fetch_page(session, link) for link in links]
            results = await asyncio.gather(*tasks)

            for link_url, link_content in results:
                if link_content:
                    with open(os.path.join('pages1', clean_url_filename(link_url) + '.html'), 'w', encoding='utf-8') as f:
                        f.write(link_content)

if __name__ == "__main__":
    asyncio.run(save_site("https://example.com"))
