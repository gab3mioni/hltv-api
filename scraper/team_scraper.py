from collections import OrderedDict
from scraper.scraper import Scraper

class TeamScraper:
    """
    Classe responsável por realizar o scraping das informações de um time no HLTV.

    A classe utiliza a biblioteca `cloudscraper` para contornar as proteções do site e `BeautifulSoup` para
    fazer o parsing do HTML da página de um time específico no HLTV. Ela coleta informações como nome, logo,
    jogadores, rankings, técnico e troféus do time.

    Atributos:
        team_id (int): ID do time no HLTV.
        team_name (str): Nome do time no HLTV.
        scraper (cloudscraper.CloudScraper): Instância do scraper para fazer as requisições HTTP.
        url (str): URL da página do time no HLTV.

    Métodos:
        __init__(team_id, team_name): Inicializa a instância da classe com os dados do time.
        get_team_info(): Retorna as informações detalhadas do time, como nome, logo, jogadores, rankings,
                        técnico e troféus.
    """

    def __init__(self, team_id, team_name):
        """
        Inicializa a instância do TeamScraper com o ID e nome do time.

        Parâmetros:
            team_id (int): ID do time.
            team_name (str): Nome do time.
        """
        self.team_id = team_id
        self.team_name = team_name
        self.url = f"https://www.hltv.org/team/{team_id}/{team_name}"
        self.scraper_instance = Scraper()

    def get_team_info(self):
        """
        Obtém as informações detalhadas do time a partir da página do HLTV.

        A função faz uma requisição HTTP à página do time, faz o parsing do HTML e extrai informações como
        nome do time, logo, jogadores, rankings, técnico e troféus, utilizando funções auxiliares.

        Retorna:
            dict: Dicionário contendo as informações do time, incluindo 'name', 'image', 'players', 
                  'valve_ranking', 'hltv_ranking', 'coach' e 'trophies'.
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
        team_name_element = soup.find('h1', class_='profile-team-name')
        return team_name_element.text.strip() if team_name_element else 'Unknown'
    
    def _get_team_logo(self, soup):
        team_logo_element = soup.find('img', class_='teamlogo')
        return team_logo_element['src'] if team_logo_element else 'Unknown'
    
    def _get_players(self, soup):
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
        valve_ranking_element = soup.find('div', class_='profile-team-stat').find('a', href=True)
        hltv_ranking_element = soup.find_all('div', class_='profile-team-stat')[1].find('a', href=True)

        valve_ranking = valve_ranking_element.text.strip() if valve_ranking_element else None
        hltv_ranking = hltv_ranking_element.text.strip() if hltv_ranking_element else None
        
        return {
            'valve_ranking': valve_ranking,
            'hltv_ranking': hltv_ranking
        }
        
    def _get_coach(self, soup):
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