import json
from flask import Flask, jsonify, Response
from scraper.team_scraper import TeamScraper
from scraper.match_scraper import MatchScraper
from scraper.event_scraper import EventScraper
from scraper.result_scraper import ResultScraper

app = Flask(__name__)

@app.route('/')
def home():
    """
    Initial endpoint that returns a welcome message.

    Returns:
        str: A message indicating that the API is up and running.
    """
    return "HLTV Web Scraping API"

@app.route('/team/<int:team_id>/<string:team_name>', methods=['GET'])
def team_info(team_id, team_name):
    """
    Endpoint that retrieves information about a specific CS2 team.

    Args:
        team_id (int): The team's ID on the HLTV website.
        team_name (str): The team's name, exactly as it appears on the HLTV website.

    Returns:
        Response: A JSON object containing the team's data.
                  If the team is not found, returns a 404 error with an appropriate message.
    """
    scraper = TeamScraper(team_id, team_name)
    team_data = scraper.get_team_info()

    if not team_data:
        return jsonify({'error': 'Team not found'}), 404
    team_json = json.dumps(team_data, ensure_ascii=False, indent=4)
    return Response(team_json, mimetype='application/json')

@app.route('/matches/<int:team_id>/<string:team_name>', methods=['GET'])
def upcoming_matches(team_id, team_name):
    """
    Endpoint that retrieves the upcoming matches for a specific CS2 team.

    Args:
        team_id (int): The team's unique ID.
        team_name (str): The team's name.

    Returns:
        Response: A JSON object containing the list of upcoming matches for the specified team.
                  If no matches are found, returns a 404 error with an appropriate message.
    """
    scraper = MatchScraper(team_id, team_name)
    matches = scraper.get_upcoming_matches()

    if not matches:
        return jsonify({'error': 'No upcoming matches found'}), 404
    matches_json = json.dumps(matches, ensure_ascii=False, indent=4)
    return Response(matches_json, mimetype='application/json')

@app.route('/events/<int:event_id>/<string:event_name>', methods=['GET'])
def event_info(event_id, event_name):
    """
    Endpoint that retrieves information about a specific CS2 event.

    Args:
        event_id (int): The event's unique ID.
        event_name (str): The event's name.

    Returns:
        Response: A JSON object containing details about the specified event.
                  If the event is not found, returns a 404 error with an appropriate message.
    """
    scraper = EventScraper(event_id, event_name)
    event_data = scraper.get_event_details()

    if not event_data:
        return jsonify({'error': 'Event not found'}), 404
    event_json = json.dumps(event_data, ensure_ascii=False, indent=4)
    return Response(event_json, mimetype='application/json')

@app.route('/result/<int:match_id>/<string:match_name>', methods=['GET'])
def result_info(match_id, match_name):
    scraper = ResultScraper(match_id, match_name)
    result_data = scraper.get_results()

    if not result_data:
        return jsonify({'error': 'Live match not found'}), 404
    result_json = json.dumps(result_data, ensure_ascii=False, indent=4)
    return Response(result_json, mimetype='application/json')

if __name__ == '__main__':
    """
    Starts the Flask server and runs the API in development mode.

    When this script is executed directly, the Flask server is launched
    with debugging enabled.
    """
    app.run(debug=True)
