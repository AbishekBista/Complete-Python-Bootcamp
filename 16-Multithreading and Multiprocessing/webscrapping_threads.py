import threading
import requests
from bs4 import BeautifulSoup


urls = [
    'https://www.google.com',
    'https://www.twitter.com',
    'https://www.facebook.com'
]

def fetchData(url):
    response = requests.get(url)
    soup  = BeautifulSoup(response.content, 'html.parser')
    print(f"Extracted {len(soup.text)} from {url}")


threads = []

for url in urls:
    thread = threading.Thread(target=fetchData, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
