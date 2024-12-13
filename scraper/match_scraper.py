import re
from collections import OrderedDict
from scraper.scraper import Scraper

class MatchScraper:
    
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name
        self.url = f"https://www.hltv.org/team/{team_id}/{team_name}"
        self.scraper_instance = Scraper()
        
    def get_upcoming_matches(self):
        """
        Obtém as próximas partidas de um time específico.

        Faz uma requisição à página de partidas futuras de um time e coleta detalhes
        sobre as partidas listadas, incluindo URLs e informações dos times participantes.

       Retorna:
           list: Uma lista de dicionários, onde cada dicionário contém os detalhes de uma partida.
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
        Obtém os detalhes de uma partida específica.

        Faz uma requisição à página de detalhes de uma partida e coleta informações como
        data, horário e detalhes dos times participantes.

        Args:
            match_url (str): URL da partida.
            team1 (str): URL do primeiro time participante.
            team2 (str): URL do segundo time participante.

        Retorna:
            dict: Um dicionário contendo os detalhes da partida, incluindo:
            - 'time': Horário da partida.
            - 'date': Data da partida.
            - 'team1': Detalhes do primeiro time (nome e logo).
            - 'team2': Detalhes do segundo time (nome e logo).
            - 'match_format': Formato da partida (LAN ou Online).
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
        date = soup.find('div', class_='date')
        return date.text.strip() if date else 'Unknown'
    
    def _get_time(self, soup):
        time = soup.find('div', class_='time')
        return time.text.strip() if time else 'Unknown'
    
    def _get_team1_details(self, soup, team1):
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
        match_format_element = soup.find('div', class_='padding preformatted-text')
        if match_format_element:
            full_text = match_format_element.text.strip()
            match_format = re.search(r'^.*?\((LAN|Online)\)', full_text)
            return match_format.group(0) if match_format else full_text
        
        return None        