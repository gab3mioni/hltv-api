import re
from collections import OrderedDict
from scraper.scraper import Scraper

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

        team_urls = self._get_team_urls(soup)

        matches = OrderedDict([
            ('match_url', f"https://www.hltv.org{team_urls['match_url']}"),
            ('details', self.get_match_details(
                f"https://www.hltv.org{team_urls['match_url']}",
                team_urls['team1_url'],
                team_urls['team2_url']
            ))
        ])

        return matches

    def get_match_details(self, match_url, team1, team2):
        """
        Fetches the details of a specific match.

        Makes a request to the match's details page and collects information such as
        date, time, and details of the participating teams.

        Args:
            match_url (str): URL of the match.
            team1 (str): URL of the first participating team.
            team2 (str): URL of the second participating team.

        Returns:
            dict: A dictionary containing the match details, including:
            - 'time': The match time.
            - 'date': The match date.
            - 'team1': Details of the first team (name and logo).
            - 'team2': Details of the second team (name and logo).
            - 'match_format': The match format (LAN or Online).
        """
        soup = self.scraper_instance.html_parser(match_url)
        match_details = OrderedDict()

        match_details['date'] = self._get_date(soup)
        match_details['time'] = self._get_time(soup)
        match_details['team1'] = self._get_team1_details(soup, team1)
        match_details['team2'] = self._get_team2_details(soup, team2)
        match_details['match_format'] = self._get_match_format(soup)

        return match_details

    def _get_team_urls(self, soup):
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
                            'match_url': f'{match_url}',
                            'team1_url': f'{team1['href']}',
                            'team2_url': f'{team2['href']}'   
                        }
        return {
            'match_url': 'Unknown',
            'team1_url': 'Unknown',
            'team2_url': 'Unknown'
        }

    def _get_date(self, soup):
        """
        Extracts the match date from the HTML.

        Args:
            soup (BeautifulSoup): Parsed HTML of the match details page.

        Returns:
            str: The match date, or 'Unknown' if not found.
        """
        date = soup.find('div', class_='date')
        return date.text.strip() if date else 'Unknown'

    def _get_time(self, soup):
        """
        Extracts the match time from the HTML.

        Args:
            soup (BeautifulSoup): Parsed HTML of the match details page.

        Returns:
            str: The match time, or 'Unknown' if not found.
        """
        time = soup.find('div', class_='time')
        return time.text.strip() if time else 'Unknown'

    def _get_team1_details(self, soup, team1):
        """
        Extracts the details of the first team from the match HTML.

        Args:
            soup (BeautifulSoup): Parsed HTML of the match details page.
            team1 (str): URL of the first team.

        Returns:
            dict: A dictionary containing the team's name and logo URL.
        """
        team1_element = soup.find('a', href=f'{team1}')
        if team1_element:
            team1_name = (
                team1_element.find('div', class_='teamName').text.strip()
                if team1_element.find('div', class_='teamName') else "Unknown"
            )
            team1_logo = (
                team1_element.find('img', class_='logo')['src']
                if team1_element.find('img', class_='logo') else None
            )
            return {
                'name': team1_name,
                'logo': team1_logo,
            } 
        return {
            'name': "Unknown", 
            'logo': None
        }

    def _get_team2_details(self, soup, team2):
        """
        Extracts the details of the second team from the match HTML.

        Args:
            soup (BeautifulSoup): Parsed HTML of the match details page.
            team2 (str): URL of the second team.

        Returns:
            dict: A dictionary containing the team's name and logo URL.
        """
        team2_element = soup.find('a', href=f'{team2}')
        if team2_element:
            team2_name = (
                team2_element.find('div', class_='teamName').text.strip()
                if team2_element.find('div', class_='teamName') else "Unknown"
            )
            team2_logo = (
               team2_element.find('img', class_='logo')['src']
                if team2_element.find('img', class_='logo') else None
            )
            return {
                'name': team2_name,
                'logo': team2_logo,
            }
        return {
            'name': "Unknown", 
            'logo': None
        }

    def _get_match_format(self, soup):
        """
        Extracts the match format (LAN or Online) from the HTML.

        Args:
            soup (BeautifulSoup): Parsed HTML of the match details page.

        Returns:
            str: The match format (e.g., "LAN" or "Online"), or None if not found.
        """
        match_format_element = soup.find('div', class_='padding preformatted-text')
        if match_format_element:
            full_text = match_format_element.text.strip()
            match_format = re.search(r'^.*?\((LAN|Online)\)', full_text)
            return match_format.group(0) if match_format else full_text

        return None
