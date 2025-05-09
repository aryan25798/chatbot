from bs4 import BeautifulSoup
import requests

def scrape_website(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    content = ' '.join(p.text for p in soup.find_all('p'))
    return content
