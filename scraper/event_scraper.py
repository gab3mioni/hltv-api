import re
from scraper.scraper import Scraper
from .interfaces.interfaces import IEventScraper

class EventScraper(IEventScraper):
    def __init__(self, event_id, event_name):
        self.event_id = event_id
        self.event_name = event_name
        self.url = f"https://www.hltv.org/events/{event_id}/{event_name}"
        self.scraper_instance = Scraper()

    def get_event_details(self):
        soup = self.scraper_instance.html_parser(self.url)
        event_details = {}

        event_details['title'] = self._get_title(soup)
        event_details['date'] = self._get_date(soup)
        event_details['prize_pool'] = self._get_prize_pool(soup)
        event_details['teams'] = self._get_teams(soup)
        event_details['location'] = self._get_location(soup)
        event_details['prize_distribution'] = self._get_prize_distribution(soup)

        return event_details

    def _get_title(self, soup):
        title = soup.find('h1', class_='event-hub-title')
        return title.text.strip() if title else 'Unknown'

    def _get_date(self, soup):
        date_element = soup.find('td', class_='eventdate')
        if date_element:
            spans = date_element.find_all('span')
            if len(spans) >= 2:
                start_date = spans[0].text.strip()
                end_date = spans[1].text.strip()
                return f"{start_date} {end_date}"
        return 'Unknown'

    def _get_prize_pool(self, soup):
        prize_pool = soup.find('td', class_='prizepool text-ellipsis')
        return prize_pool.text.strip() if prize_pool else 'Unknown'

    def _get_teams(self, soup):
        teams = soup.find_all('td', class_='teamsNumber')
        return teams[0].text.strip() if teams else 'Unknown'

    def _get_location(self, soup):
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