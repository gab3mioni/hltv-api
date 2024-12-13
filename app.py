import json
from flask import Flask, jsonify, Response
from scraper.team_scraper import TeamScraper
from scraper.match_scraper import MatchScraper
from scraper.event_scraper import EventScraper

app = Flask(__name__)

@app.route('/')
def home():
    """
    Endpoint inicial que retorna uma mensagem de boas-vindas.

    Returns:
        str: Mensagem indicando que a API está funcionando.
    """
    return "HLTV Web Scraping API"

@app.route('/team/<int:team_id>/<string:team_name>', methods=['GET'])
def team_info(team_id, team_name):
    """
    Endpoint que retorna as informações de um time de CS2 específico.

    Parâmetros:
        team_id (int): O ID do time no site HLTV.
        team_name (string): O nome do time (exato como aparece no site HLTV).

    Returns:
        json: Dados do time em formato JSON. Em caso de erro (time não encontrado),
              retorna um erro 404 com uma mensagem.
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
    Busca as próximas partidas de um time específico pelo seu ID e nome.

    Args:
        team_id (int): O ID único do time.
        team_name (str): O nome do time.

    Retorna:
        Response: Uma resposta JSON contendo a lista de próximas partidas do time especificado.
                  Se nenhuma partida for encontrada, retorna um status 404 com uma mensagem de erro.
    """
    scraper = MatchScraper(team_id, team_name)
    matches = scraper.get_upcoming_matches()

    if not matches:
        return jsonify({'error': 'Nenhuma partida futura encontrada'}), 404
    matches_json = json.dumps(matches, ensure_ascii=False, indent=4)
    return Response(matches_json, mimetype='application/json')

@app.route('/events/<int:event_id>/<string:event_name>', methods=['GET'])
def event_info(event_id, event_name):
    """
    Busca informações sobre um evento de CS2 específico.

    Args:
        event_id (int): O ID único do evento.
        event_name (str): O nome do evento.

    Retorna:
        Response: Uma resposta JSON contendo detalhes sobre o evento especificado.
                  Se o evento não for encontrado, retorna um status 404 com uma mensagem de erro.
    """
    scraper = EventScraper(event_id, event_name)
    event_data = scraper.get_event_details()

    if not event_data:
        return jsonify({'error': 'Evento não encontrado'}), 404
    event_json = json.dumps(event_data, ensure_ascii=False, indent=4)
    return Response(event_json, mimetype='application/json')

if __name__ == '__main__':
    """
    Inicia o servidor Flask, rodando a API em modo de desenvolvimento.

    Quando o script é executado diretamente, o servidor Flask é iniciado
    com a configuração de debug ativada.
    """
    app.run(debug=True)
