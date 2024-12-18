import re
from collections import OrderedDict

def get_match_details(scraper_instance, match_url, team1, team2):
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
    soup = scraper_instance.html_parser(match_url)
    match_details = OrderedDict()

    match_details['date'] = _get_date(soup)
    match_details['time'] = _get_time(soup)
    match_details['team1'] = _get_team1_details(soup, team1)
    match_details['team2'] = _get_team2_details(soup, team2)
    match_details['match_format'] = _get_match_format(soup)

    return match_details
    
def _get_date(soup):
    """
    Extracts the match date from the HTML.

    Args:
       soup (BeautifulSoup): Parsed HTML of the match details page.

    Returns:
        str: The match date, or 'Unknown' if not found.
    """
    date = soup.find('div', class_='date')
    return date.text.strip() if date else 'Unknown'

def _get_time(soup):
    """
    Extracts the match time from the HTML.

    Args:
        soup (BeautifulSoup): Parsed HTML of the match details page.

    Returns:
        str: The match time, or 'Unknown' if not found.
    """
    time = soup.find('div', class_='time')
    return time.text.strip() if time else 'Unknown'

def _get_team1_details(soup, team1):
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

def _get_team2_details(soup, team2):
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

def _get_match_format(soup):
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
