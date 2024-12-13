from collections import OrderedDict
from scraper.scraper import Scraper

class TeamScraper:
    """
    A class to scrape information about a team from the HLTV.

    Attributes:
        team_id (str): The unique ID of the team.
        team_name (str): The name of the team.
        url (str): The URL to the team page on HLTV.
        scraper_instance (Scraper): An instance of the Scraper class to fetch and parse the HTML.

    Methods:
        get_team_info(): Scrapes and returns the team information, including name, logo, players, rankings, coach, and trophies.
        _get_team_name(soup): Extracts the team name from the parsed HTML.
        _get_team_logo(soup): Extracts the team logo URL from the parsed HTML.
        _get_players(soup): Extracts information about the players, including nickname, flag, image, and title.
        _get_rankings(soup): Extracts the team Valve and HLTV rankings.
        _get_coach(soup): Extracts the coach nickname and flag.
        _get_trophies(soup): Extracts information about the team's trophies, including title, image, and URL.
    """
    def __init__(self, team_id, team_name):
        """
        Initializes the TeamScraper instance with a team ID and team name.

        Args:
            team_id (str): The unique ID of the team.
            team_name (str): The name of the team.
        """
        self.team_id = team_id
        self.team_name = team_name
        self.url = f"https://www.hltv.org/team/{team_id}/{team_name}"
        self.scraper_instance = Scraper()

    def get_team_info(self):
        """
        Scrapes and returns the team's information from the HLTV website.

        Returns:
            OrderedDict: A dictionary containing the team's name, logo, players, rankings, coach, and trophies.
        """
        soup = self.scraper_instance.html_parser(self.url)
        team_info = OrderedDict([
            ('name', self._get_team_name(soup)),
            ('image', self._get_team_logo(soup)),
            ('players', self._get_players(soup)),
            ('ranking', self._get_rankings(soup)),
            ('coach', self._get_coach(soup)),
            ('trophies', self._get_trophies(soup))
        ])

        return team_info
    
    def _get_team_name(self, soup):
        """
        Extracts the team name from the parsed HTML.

        Args:
            soup (BeautifulSoup): The parsed HTML of the team's page.

        Returns:
            str: The team name, or 'Unknown' if the name is not found.
        """
        team_name_element = soup.find('h1', class_='profile-team-name')
        return team_name_element.text.strip() if team_name_element else 'Unknown'
    
    def _get_team_logo(self, soup):
        """
        Extracts the team logo URL from the parsed HTML.

        Args:
            soup (BeautifulSoup): The parsed HTML of the team's page.

        Returns:
            str: The team logo URL, or 'Unknown' if the logo is not found.
        """
        team_logo_element = soup.find('img', class_='teamlogo')
        return team_logo_element['src'] if team_logo_element else 'Unknown'
    
    def _get_players(self, soup):
        """
        Extracts information about the players, including nickname, flag, image, and title.

        Args:
            soup (BeautifulSoup): The parsed HTML of the team's page.

        Returns:
            list: A list of dictionaries containing player information (nickname, flag, image, title).
        """
        players = []
        player_containers = soup.find_all('div', class_='bodyshot-team')[0].find_all('a', class_='col-custom')
        for player_container in player_containers:
            player_nick = player_container.find('div', class_='playerFlagName').find('span', class_='bold')
            player_flag = player_container.find('img', class_='flag')
            player_image = player_container.find('img', class_='bodyshot-team-img')
            if player_nick and player_flag and player_image:
                players.append({
                    'nickname': player_nick.text.strip(),
                    'flag': "https://www.hltv.org" + player_flag['src'],
                    'image': player_image['src'],
                    'title': player_image['title']
                })
            else:
                players.append({
                    'nickname': 'Unknown',
                    'flag': 'Unknown',
                    'image': 'Unknown',
                    'title': 'Unknown'
                })
        
        return players
        
    def _get_rankings(self, soup):
        """
        Extracts the team's Valve and HLTV rankings from the parsed HTML.

        Args:
            soup (BeautifulSoup): The parsed HTML of the team's page.

        Returns:
            dict: A dictionary containing the Valve and HLTV rankings.
        """
        valve_ranking_element = soup.find('div', class_='profile-team-stat').find('a', href=True)
        hltv_ranking_element = soup.find_all('div', class_='profile-team-stat')[1].find('a', href=True)

        valve_ranking = valve_ranking_element.text.strip() if valve_ranking_element else None
        hltv_ranking = hltv_ranking_element.text.strip() if hltv_ranking_element else None
        
        return {
            'valve_ranking': valve_ranking,
            'hltv_ranking': hltv_ranking
        }
        
    def _get_coach(self, soup):
        """
        Extracts the coach's nickname and flag from the parsed HTML.

        Args:
            soup (BeautifulSoup): The parsed HTML of the team's page.

        Returns:
            dict: A dictionary containing the coach's nickname and flag.
        """
        coach_element = soup.find('div', class_='profile-team-stats-container').find('a', class_='a-reset')
        if coach_element:
            coach_name = coach_element.find('span', class_='bold a-default')
            coach_flag = coach_element.find('img', class_='flag')
            if coach_name and coach_flag:
                return {
                    'nickname': coach_name.text.strip().strip("'"),
                    'flag': "https://www.hltv.org" + coach_flag['src']
                }
                
        return {
            'nickname': 'Unknown',
            'flag': 'Unknown'
        }
        
    def _get_trophies(self, soup):
        """
        Extracts information about the team's trophies, including title, image, and URL.

        Args:
            soup (BeautifulSoup): The parsed HTML of the team's page.

        Returns:
            list: A list of dictionaries containing trophy information (title, image, URL).
        """
        trophy_containers = soup.find_all('div', class_='trophyRow')
        trophies = []
        
        for trophy_container in trophy_containers[0].find_all('a', class_='trophy'):
            trophy_url = trophy_container['href']
            trophy_title = trophy_container.find('span', class_='trophyDescription')['title']
            trophy_image = trophy_container.find('img', class_='trophyIcon')['src']
                
            if trophy_title and trophy_image:
                trophies.append({
                    'title': trophy_title,
                    'image': trophy_image,
                    'url': f"https://www.hltv.org{trophy_url}"
                })
            else:
                trophies.append({
                    'title': 'Unknown',
                    'image': 'Unknown',
                    'url': 'Unknown'
                })
    
        return trophies