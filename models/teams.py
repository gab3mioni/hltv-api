class Team:
    """
    Classe que representa um time de CS2.

    A classe armazena informações detalhadas sobre um time, como nome, imagem, jogadores, rankings,
    técnico e troféus. Ela também fornece um método para converter essas informações em um dicionário
    para fácil manipulação ou exportação.

    Atributos:
        name (str): Nome do time.
        image (str): URL da imagem do logo do time.
        players (list): Lista de jogadores do time.
        valve_ranking (str): Ranking do time no sistema da Valve.
        hltv_ranking (str): Ranking do time no HLTV.
        coach (dict): Informações sobre o técnico do time, incluindo nome e bandeira.
        trophies (list): Lista de troféus do time, incluindo título e imagem.

    Métodos:
        __init__(name, image, players, valve_ranking, hltv_ranking, coach, trophies):
            Inicializa uma instância da classe com os dados do time.
        
        to_dict():
            Converte as informações do time em um dicionário.
    """

    def __init__(self, name, image, players, valve_ranking, hltv_ranking, coach, trophies):
        """
        Inicializa a instância do time com informações detalhadas.

        Parâmetros:
            name (str): Nome do time.
            image (str): URL da imagem do logo do time.
            players (list): Lista de jogadores do time.
            valve_ranking (str): Ranking do time no sistema da Valve.
            hltv_ranking (str): Ranking do time no HLTV.
            coach (dict): Informações sobre o técnico do time, incluindo nome e bandeira.
            trophies (list): Lista de troféus do time, incluindo título e imagem.
        """
        self.name = name
        self.image = image
        self.players = players
        self.valve_ranking = valve_ranking
        self.hltv_ranking = hltv_ranking
        self.coach = coach
        self.trophies = trophies

    def to_dict(self):
        """
        Converte as informações do time para um dicionário.

        Retorna:
            dict: Dicionário contendo todas as informações do time, incluindo 'name', 'image', 'players',
                  'valve_ranking', 'hltv_ranking', 'coach' e 'trophies'.
        """
        return {
            'name': self.name,
            'image': self.image,
            'players': self.players,
            'valve_ranking': self.valve_ranking,
            'hltv_ranking': self.hltv_ranking,
            'coach': self.coach,
            'trophies': self.trophies
        }
