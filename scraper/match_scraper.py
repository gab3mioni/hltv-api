from collections import OrderedDict
from scraper.scraper import Scraper
from utils.match_utils import get_match_details

class MatchScraper:
    """
    Scraper class to fetch and parse match details for a specific team from HLTV.
    
    Attributes:
        team_id (int): The ID of the team.
        team_name (str): The name of the team.
        url (str): The base URL for the team's matches page on HLTV.
        scraper_instance (Scraper): Instance of the scraper utility.
    """

    def __init__(self, team_id, team_name):
        """
        Initializes the MatchScraper with team ID and name.

        Args:
            team_id (int): The ID of the team.
            team_name (str): The name of the team.
        """
        self.team_id = team_id
        self.team_name = team_name
        self.url = f"https://www.hltv.org/team/{team_id}/{team_name}"
        self.scraper_instance = Scraper()

    def get_upcoming_matches(self):
        """
        Fetches the upcoming matches for the team.

        Makes a request to the team's upcoming matches page and collects details
        about the matches listed, including URLs and information about participating teams.

        Returns:
            list: A list of dictionaries, where each dictionary contains the details of a match.
        """
        match_url = f"{self.url}#tab-matchesBox"
        soup = self.scraper_instance.html_parser(match_url)

        team_url = self._get_match_url(soup)
        
        if team_url['match_url'] == 'Unknown':
            return []

        matches = OrderedDict([
            ('match_url', f"https://www.hltv.org{team_url['match_url']}"),
            ('details', self.get_details(
                f"https://www.hltv.org{team_url['match_url']}", f"{team_url['team1_url']}", f"{team_url['team2_url']}",
            ))
        ])

        return matches


    def _get_match_url(self, soup):
        """
        Extracts the URLs of the participating teams from the match container.

        Args:
            soup (BeautifulSoup): Parsed HTML of the team's matches page.

        Returns:
            dict: A dictionary containing the match URL and team URLs.
        """
        matches_container = soup.find('div', id='matchesBox')
        if matches_container:
            match_elements = matches_container.find_all('tr', class_='team-row')

            for match in match_elements:
                match_button = match.find('a', class_='matchpage-button')
                if match_button:
                    match_url = match_button['href']
                    team1 = match.find('a', class_='team-name team-1')
                    team2 = match.find('a', class_='team-name team-2')

                    if team1 and team2:
                        return {
                            "match_url": f"{match_url}",
                            "team1_url": f"{team1['href']}",
                            "team2_url": f"{team2['href']}"
                        }               

        return {
            'match_url': 'Unknown',
            'team1_url': 'Unknown',
            'team2_url': 'Unknown'
        }
        
    def get_details(self, match_url, team1, team2):
        return get_match_details(self.scraper_instance, match_url, team1, team2)