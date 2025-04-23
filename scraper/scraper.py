import cloudscraper
from bs4 import BeautifulSoup

class Scraper:
    """
    A class to facilitate web scraping by using CloudScraper to bypass anti-bot mechanisms and BeautifulSoup for HTML parsing.

    Attributes:
        scraper (CloudScraper): An instance of the CloudScraper library used to handle HTTP requests.
    """
    
    def __init__(self):
        """
        Initializes the Scraper instance and creates a CloudScraper object for HTTP requests.
        """
        self.scraper = cloudscraper.create_scraper()
        
    def html_parser(self, url):
        """
        Fetches the HTML content of a given URL and parses it using BeautifulSoup.

        Args:
            url (str): The URL of the webpage to scrape.

        Returns:
            BeautifulSoup: A BeautifulSoup object representing the parsed HTML content of the page.
        """
        response = self.scraper.get(url)
        
        if response.status_code != 200:
            print(f"[ERRO] Status {response.status_code} ao acessar {url}")
            return None

        with open("/tmp/debug_page.html", "w", encoding="utf-8") as f:
            f.write(response.text)
            
        return BeautifulSoup(response.text, 'html.parser')