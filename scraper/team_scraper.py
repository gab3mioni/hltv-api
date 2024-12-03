import cloudscraper
from bs4 import BeautifulSoup
from models.teams import Team
from utils.scraper_utils import parse_players, parse_rankings, parse_coach, parse_trophies

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
        self.scraper = cloudscraper.create_scraper()
        self.url = f"https://www.hltv.org/team/{team_id}/{team_name}"

    def get_team_info(self):
        """
        Obtém as informações detalhadas do time a partir da página do HLTV.

        A função faz uma requisição HTTP à página do time, faz o parsing do HTML e extrai informações como
        nome do time, logo, jogadores, rankings, técnico e troféus, utilizando funções auxiliares.

        Retorna:
            dict: Dicionário contendo as informações do time, incluindo 'name', 'image', 'players', 
                  'valve_ranking', 'hltv_ranking', 'coach' e 'trophies'. Retorna `None` se não encontrar
                  o nome do time na página.
        """
        response = self.scraper.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        team_info = {}

        # Parse basic team info
        team_name_element = soup.find('h1', class_='profile-team-name')
        if team_name_element:
            team_info['name'] = team_name_element.text.strip()
        else:
            return None
        
        team_logo_element = soup.find('img', class_='teamlogo')
        if team_logo_element:
            team_info['image'] = team_logo_element['src']

        # Parse additional details
        team_info['players'] = parse_players(soup)
        team_info['valve_ranking'], team_info['hltv_ranking'] = parse_rankings(soup)
        team_info['coach'] = parse_coach(soup)
        team_info['trophies'] = parse_trophies(soup)

        return team_info
