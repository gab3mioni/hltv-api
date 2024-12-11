import re
from scraper.scraper import Scraper

class MatchScraper:
    
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name
        self.url = f"https://www.hltv.org/team/{team_id}/{team_name}"
        
    def get_upcoming_matches(self):
        """
        Obtém as próximas partidas de um time específico.

        Faz uma requisição à página de partidas futuras de um time e coleta detalhes
        sobre as partidas listadas, incluindo URLs e informações dos times participantes.

       Retorna:
           list: Uma lista de dicionários, onde cada dicionário contém os detalhes de uma partida.
        """
        scraper_instance = Scraper()
        match_url = f"{self.url}#tab-matchesBox"
        soup = scraper_instance.html_parser(match_url)
        matches = {}

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
                        team1_url = team1['href']
                        team2_url = team2['href']

                        match_details = self.get_match_details(
                            f"https://www.hltv.org{match_url}", team1_url, team2_url
                        )

                        matches[match_url] = match_details

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
        """
        scraper_instance = Scraper()
        soup = scraper_instance.html_parser(match_url)
        match_details = {}

        time = soup.find('div', class_='time')
        date = soup.find('div', class_='date')

        if time and date:
            match_details['time'] = time.text.strip()
            match_details['date'] = date.text.strip()
        else:
            match_details['time'] = None
            match_details['date'] = None

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
            match_details['team1'] = {
                'name': team1_name,
                'logo': team1_logo,
            }
        else:
            match_details['team1'] = {'name': "Unknown", 'logo': None}

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
            match_details['team2'] = {
                'name': team2_name,
                'logo': team2_logo,
            }
        else:
            match_details['team2'] = {'name': "Unknown", 'logo': None}
            
        match_format_element = soup.find('div', class_='padding preformatted-text')
        if match_format_element:
            full_text = match_format_element.text.strip()
            match_format = re.search(r'^.*?\((LAN|Online)\)', full_text)
            match_details['match_format'] = match_format.group(0) if match_format else full_text
        else:
            match_details['match_format'] = None

        return match_details