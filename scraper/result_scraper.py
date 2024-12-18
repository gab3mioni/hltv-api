from collections import OrderedDict
from scraper.scraper import Scraper
from utils.match_utils import get_match_details

class ResultScraper:
    
    def __init__(self, match_id, match_name):
        self.match_id = match_id
        self.match_name = match_name
        self.url = f"https://www.hltv.org/matches/{match_id}/{match_name}"
        self.scraper_instance = Scraper()
        
    def get_results(self):
        soup = self.scraper_instance.html_parser(self.url)
        
        teams_url = self._get_teams_url(soup)
        maps = self._get_maps(soup)
        
        results = OrderedDict([
            ('details', self.get_details(self.url, teams_url.get('team1'), teams_url.get('team2'))),
            ('maps', maps)
        ])
        
        return results
    
    def _get_teams_url(self, soup):
        def extract_url(team_class):
            team = soup.find('a', class_=team_class)
            return team['href'] if team and 'href' in team.attrs else None

        return {
            'team1': extract_url('team1'),
            'team2': extract_url('team2')
        }

    def _get_maps(self, soup):
        maps = []


        map_containers = soup.find_all('div', class_='mapholder')

        for container in map_containers:
            map_name_div = container.find('div', class_='mapname')
            map_name = map_name_div.text.strip() if map_name_div else "Unknown"

            results_left = container.find('div', class_='results-left')
            results_right = container.find('span', class_='results-right')
            
            team1_score = (
                results_left.find('div', class_='results-team-score').text.strip()
                if results_left and results_left.find('div', class_='results-team-score') else "-"
            )
            team2_score = (
                results_right.find('div', class_='results-team-score').text.strip()
                if results_right and results_right.find('div', class_='results-team-score') else "-"
            )

            maps.append({
                'map': map_name,
                'team1_score': team1_score,
                'team2_score': team2_score
            })

        return maps

    def get_details(self, match_url, team1, team2):
        return get_match_details(self.scraper_instance, match_url, team1, team2)