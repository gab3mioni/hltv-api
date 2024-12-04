from flask import Flask, jsonify
from scraper.team_scraper import TeamScraper

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
    Endpoint que retorna as informações de um time de e-sports específico.

    Este endpoint faz scraping do site HLTV.org para obter detalhes sobre
    o time, como jogadores, ranking, próximas partidas, resultados passados, etc.

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
    return jsonify(team_data)

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
    scraper = TeamScraper(team_id, team_name)
    matches = scraper.get_upcoming_matches()

    if not matches:
        return jsonify({'error': 'Nenhuma partida futura encontrada'}), 404
    return jsonify(matches)

if __name__ == '__main__':
    """
    Inicia o servidor Flask, rodando a API em modo de desenvolvimento.

    Quando o script é executado diretamente, o servidor Flask é iniciado
    com a configuração de debug ativada.
    """
    app.run(debug=True)
