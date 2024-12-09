def parse_players(soup):
    """
    Extrai e retorna a lista de jogadores de um time a partir do conteúdo HTML da página do time.

    A função procura os elementos HTML relacionados aos jogadores, como o nome do jogador, 
    a URL da bandeira do país, a imagem do jogador e o título associado. Cada jogador é representado por 
    um dicionário contendo estas informações.

    Parâmetros:
        soup (BeautifulSoup): Objeto BeautifulSoup contendo o HTML da página do time.

    Retorna:
        list: Lista de dicionários, onde cada dicionário representa um jogador e contém as chaves:
            - 'nickname' (str): Nome do jogador.
            - 'flag' (str): URL da imagem da bandeira do país do jogador.
            - 'image' (str): URL da imagem do jogador.
            - 'title' (str): Texto do atributo 'title' associado à imagem do jogador.
    """
    players = []
    try:
        player_containers = soup.find_all('div', class_='bodyshot-team')[0].find_all('a', class_='col-custom')
        for player_container in player_containers:
            try:
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
            except Exception as e:
                print(f"Erro ao processar jogador: {e}")
    except Exception as e:
        print(f"Erro ao buscar jogadores: {e}")
    return players

def parse_rankings(soup):
    """
    Extrai os rankings Valve e HLTV de um time a partir do conteúdo HTML da página do time.

    A função encontra os elementos HTML que contêm o ranking do time tanto no sistema Valve quanto no HLTV.

    Parâmetros:
        soup (BeautifulSoup): Objeto BeautifulSoup contendo o HTML da página do time.

    Retorna:
        tuple: Tupla contendo o ranking Valve e o ranking HLTV, onde ambos podem ser `None` se não encontrados.
    """
    try:
        valve_ranking_element = soup.find('div', class_='profile-team-stat').find('a', href=True)
        hltv_ranking_element = soup.find_all('div', class_='profile-team-stat')[1].find('a', href=True)

        valve_ranking = valve_ranking_element.text.strip() if valve_ranking_element else None
        hltv_ranking = hltv_ranking_element.text.strip() if hltv_ranking_element else None
        return valve_ranking, hltv_ranking
    except Exception as e:
        print(f"Erro ao buscar rankings: {e}")
        return None, None

def parse_coach(soup):
    """
    Extrai as informações do técnico (nome e bandeira) de um time a partir do conteúdo HTML da página do time.

    A função encontra o elemento HTML que contém o nome e a bandeira do técnico, caso exista.

    Parâmetros:
        soup (BeautifulSoup): Objeto BeautifulSoup contendo o HTML da página do time.

    Retorna:
        dict: Dicionário contendo o nome e a bandeira do técnico, ou `None` se o técnico não for encontrado.
    """
    try:
        coach_element = soup.find('div', class_='profile-team-stats-container').find('a', class_='a-reset')
        if coach_element:
            coach_name = coach_element.find('span', class_='bold a-default')
            coach_flag = coach_element.find('img', class_='flag')
            if coach_name and coach_flag:
                return {
                    'nickname': coach_name.text.strip().strip("'"),
                    'flag': "https://www.hltv.org" + coach_flag['src']
                }
        return None
    except Exception as e:
        print(f"Erro ao buscar informações do técnico: {e}")
        return None

def parse_trophies(soup):
    """
    Extrai os troféus conquistados por um time a partir do conteúdo HTML da página do time.

    A função busca os elementos HTML que contêm as informações sobre os troféus, como título e imagem.

    Parâmetros:
        soup (BeautifulSoup): Objeto BeautifulSoup contendo o HTML da página do time.

    Retorna:
        list: Lista de dicionários, cada um representando um troféu com 'title' e 'image'.
    """
    trophies = []
    try:
        trophy_containers = soup.find_all('div', class_='trophyRow')
        if not trophy_containers:
            return []

        for trophy_container in trophy_containers[0].find_all('a', class_='trophy'):
            try:
                trophy_title = trophy_container.find('span', class_='trophyDescription')['title']
                trophy_image = trophy_container.find('img', class_='trophyIcon')['src']
                trophies.append({
                    'title': trophy_title,
                    'image': trophy_image
                })
            except Exception as e:
                print(f"Erro ao processar troféu: {e}")
    except Exception as e:
        print(f"Erro ao buscar troféus: {e}")
    return trophies
