import cloudscraper
from bs4 import BeautifulSoup

class Scraper:
    
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()
        
    def html_parser(self, url):
        response = self.scraper.get(url)
        return BeautifulSoup(response.text, 'html.parser')