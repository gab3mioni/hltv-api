import re
from collections import OrderedDict
from scraper.scraper import Scraper

class EventScraper:
    """
    A class to scrape event details from HLTV.

    Attributes:
        event_id (int): The unique ID of the event.
        event_name (str): The name of the event.
        url (str): The URL to the event.
        scraper_instance (Scraper): An instance of the Scraper class to fetch and parse the HTML.
    """

    def __init__(self, event_id, event_name):
        """
        Initializes the EventScraper with the event ID and name, and sets up the URL and scraper instance.

        Args:
            event_id (int): The unique identifier of the event.
            event_name (str): The name of the event.
        """
        self.event_id = event_id
        self.event_name = event_name
        self.url = f"https://www.hltv.org/events/{event_id}/{event_name}"
        self.scraper_instance = Scraper()

    def get_event_details(self):
        """
        Retrieves event details such as title, date, prize pool, teams, location, and prize distribution.

        Returns:
            OrderedDict: A dictionary containing the event details.
        """
        soup = self.scraper_instance.html_parser(self.url)
        event_details = OrderedDict([
            ('title', self._get_title(soup)),
            ('date', self._get_date(soup)),
            ('prize_pool', self._get_prize_pool(soup)),
            ('teams', self._get_teams(soup)),
            ('location', self._get_location(soup)),
            ('prize_distribution', self._get_prize_distribution(soup))
        ])
        return event_details

    def _get_title(self, soup):
        """
        Extracts the title of the event.

        Args:
            soup (BeautifulSoup): The parsed HTML of the event page.

        Returns:
            str: The event title, or 'Unknown' if not found.
        """
        title = soup.find('h1', class_='event-hub-title')
        return title.text.strip() if title else 'Unknown'

    def _get_date(self, soup):
        """
        Extracts the start and end dates of the event.

        Args:
            soup (BeautifulSoup): The parsed HTML of the event page.

        Returns:
            str: The event dates, or 'Unknown' if not found.
        """
        date_element = soup.find('td', class_='eventdate')
        if date_element:
            spans = date_element.find_all('span')
            if len(spans) >= 2:
                start_date = spans[0].text.strip()
                end_date = spans[1].text.strip()
                return f"{start_date} {end_date}"
        return 'Unknown'

    def _get_prize_pool(self, soup):
        """
        Extracts the prize pool for the event.

        Args:
            soup (BeautifulSoup): The parsed HTML of the event page.

        Returns:
            str: The prize pool, or 'Unknown' if not found.
        """
        prize_pool = soup.find('td', class_='prizepool text-ellipsis')
        return prize_pool.text.strip() if prize_pool else 'Unknown'

    def _get_teams(self, soup):
        """
        Extracts the number of teams participating in the event.

        Args:
            soup (BeautifulSoup): The parsed HTML of the event page.

        Returns:
            str: The number of teams, or 'Unknown' if not found.
        """
        teams = soup.find_all('td', class_='teamsNumber')
        return teams[0].text.strip() if teams else 'Unknown'

    def _get_location(self, soup):
        """
        Extracts the location and type (LAN or Online) of the event.

        Args:
            soup (BeautifulSoup): The parsed HTML of the event page.

        Returns:
            dict: A dictionary containing the flag URL, location, and event type.
        """
        location_element = soup.find('div', class_='flag-align')
        if location_element:
            flag_img = location_element.find('img', class_='flag')
            location_text = location_element.find('span', class_='text-ellipsis').text.strip()
            location_match = re.search(r'^(.*) \((LAN|Online)\)$', location_text)
            if location_match:
                location = location_match.group(1)
                event_type = location_match.group(2)
            else:
                location = location_text
                event_type = 'Unknown'
            return {
                'flag': f"https://www.hltv.org{flag_img['src']}" if flag_img else 'Unknown',
                'location': location,
                'type': event_type
            }
        return {
            'flag': 'Unknown',
            'location': 'Unknown',
            'type': 'Unknown'
        }

    def _get_prize_distribution(self, soup):
        """
        Extracts the prize distribution for the event.

        Args:
            soup (BeautifulSoup): The parsed HTML of the event page.

        Returns:
            dict: A dictionary containing prize distribution details by placement.
        """
        prize_distribution = {}
        placements_holder = soup.find('div', class_='placements-holder')
        if placements_holder:
            placements = placements_holder.find_all('div', class_='placement')
            for placement in placements:
                position = placement.find_all('div')[1].text.strip() if len(placement.find_all('div')) > 1 else 'Unknown'
                team_element = placement.find('div', class_='team')
                if team_element and team_element.find('a'):
                    team_name = team_element.find('a').text.strip()
                    team_logo = placement.find('div', class_='team-logo').find('img')['src'] if placement.find('div', class_='team-logo') else 'Unknown'
                    prizes = [prize.text.strip() for prize in placement.find_all('div', class_='prize') if prize.text.strip()]
                    if position not in prize_distribution:
                        prize_distribution[position] = []
                    prize_distribution[position].append({
                        'team_name': team_name,
                        'team_logo': team_logo,
                        'prizes': prizes
                    })
                else:
                    prizes = [prize.text.strip() for prize in placement.find_all('div', class_='prize') if prize.text.strip()]
                    if position not in prize_distribution:
                        prize_distribution[position] = []
                    prize_distribution[position].append({
                        'prizes': prizes
                    })
        return prize_distribution
