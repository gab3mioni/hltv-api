import cloudscraper
from bs4 import BeautifulSoup

class Scraper:
    
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name
        self.scraper = cloudscraper.create_scraper()
        self.url = f"https://www.hltv.org/team/{team_id}/{team_name}"
        
    def html_parser(self, url):
        response = self.scraper.get(url)
        return BeautifulSoup(response.text, 'html.parser')