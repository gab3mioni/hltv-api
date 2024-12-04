# HLTV Web Scraping API

This project provides a simple API built with Flask that scrapes information from the [HLTV.org](https://www.hltv.org) website. The API allows users to retrieve detailed information about a specific e-sports team based on their team ID or name.

## Features

The API provides the following information for a given e-sports team:
- **Team Name**
- **Team Logo Image**
- **Player Names and Flags**
- **Valve Ranking**
- **HLTV Ranking**
- **Coach Name and Flag**
- **Team Trophies**
- **Upcoming Matches**

## Endpoints

### `GET /team/<team_id>/<team_name>`

This endpoint retrieves detailed information about the team identified by its **team ID** and **team name**.

#### Parameters:
- `team_id` (integer): The ID of the team on HLTV.org.
- `team_name` (string): The name of the team (use the exact team name from the URL on HLTV.org).

#### Example Request:

GET /team/8297/furia

```json
{
    "coach": {
        "flag": "https://www.hltv.org/img/static/flags/30x20/BR.gif",
        "nickname": "sidde"
    },
    "hltv_ranking": "#8",
    "image": "https://img-cdn.hltv.org/teamlogo/mvNQc4csFGtxXk5guAh8m1.svg?ixlib=java-2.1.0&s=11e5056829ad5d6c06c5961bbe76d20c",
    "name": "FURIA",
    "players": [
        {
            "flag": "https://www.hltv.org/img/static/flags/30x20/BR.gif",
            "image": "https://img-cdn.hltv.org/playerbodyshot/Wf26SO_o8nvnsLh0AqZXc5.png?ixlib=java-2.1.0&w=400&s=36b7189a4ae7b020d0acb087fd44777a",
            "nickname": "FalleN",
            "title": "Gabriel 'FalleN' Toledo"
        },
        {
            "flag": "https://www.hltv.org/img/static/flags/30x20/BR.gif",
            "image": "https://img-cdn.hltv.org/playerbodyshot/1UmLZkSSAfBosakeRR3gwZ.png?ixlib=java-2.1.0&w=400&s=4b513eb29f7896053a6996ef30575ed8",
            "nickname": "chelo",
            "title": "Marcelo 'chelo' Cespedes"
        },
        {
            "flag": "https://www.hltv.org/img/static/flags/30x20/BR.gif",
            "image": "https://img-cdn.hltv.org/playerbodyshot/i6UGhkYxrhutAOmWZT0-8O.png?ixlib=java-2.1.0&w=400&s=2cd696f6ff4baf5680a43d537214b6eb",
            "nickname": "yuurih",
            "title": "Yuri 'yuurih' Santos"
        },
        {
            "flag": "https://www.hltv.org/img/static/flags/30x20/BR.gif",
            "image": "https://img-cdn.hltv.org/playerbodyshot/U6t0j2bJDKUR3mTI8rIqv7.png?ixlib=java-2.1.0&w=400&s=b5257c378b8122f415f21985855e95ca",
            "nickname": "KSCERATO",
            "title": "Kaike 'KSCERATO' Cerato"
        },
        {
            "flag": "https://www.hltv.org/img/static/flags/30x20/BR.gif",
            "image": "https://img-cdn.hltv.org/playerbodyshot/Ql8Oez5CfB2SBPOQdLJdL3.png?ixlib=java-2.1.0&w=400&s=780116a9290d11b1347f35182716ad53",
            "nickname": "skullz",
            "title": "Felipe 'skullz' Medeiros"
        }
    ],
    "trophies": [
        {
            "image": "https://img-cdn.hltv.org/eventtrophy/YXUTz-Lpcm8MjEgmdjZk7u.png?ixlib=java-2.1.0&w=200&s=35b769e3537ae9f3f7151d60a7981190",
            "title": "Elisa Masters Espoo 2023"
        },
        {
            "image": "https://img-cdn.hltv.org/eventlogo/dxrSBtNp6X_5sEX_RtI-9F.png?ixlib=java-2.1.0&w=50&s=4495ad07a9c3477df3ddaab1ca012d0e",
            "title": "IEM New York 2020 North America"
        },
        {
            "image": "/img/static/event/trophies/5495.png",
            "title": "ESL Pro League Season 12 North America"
        },
        {
            "image": "https://img-cdn.hltv.org/eventlogo/6eIN1Gj-8Gn6UtQA4Jj5bt.png?ixlib=java-2.1.0&w=50&s=27a0947475d35ec2dd40499c75f77d15",
            "title": "DreamHack Masters Spring 2020 - North America"
        }
    ],
    "valve_ranking": "#10"
}
```

### `GET /matches/<team_id>/<team_name>`

This endpoint retrieves detailed information about the next matches schedules from team identified by its **team ID** and **team name**.

#### Parameters:
- `team_id` (integer): The ID of the team on HLTV.org.
- `team_name` (string): The name of the team (use the exact team name from the URL on HLTV.org).

#### Example Request:

GET /matches/8297/furia

```json
{
    "/matches/2377699/spirit-vs-furia-perfect-world-shanghai-major-2024": {
        "date": "5 Dec",
        "team1": {
            "logo": "https://img-cdn.hltv.org/teamlogo/mvNQc4csFGtxXk5guAh8m1.svg?ixlib=java-2.1.0&s=11e5056829ad5d6c06c5961bbe76d20c",
            "name": "FURIA"
        },
        "team2": {
            "logo": "https://img-cdn.hltv.org/teamlogo/syrtYYKR7sBRw3ZHy1YFX7.png?ixlib=java-2.1.0&w=100&s=8d98ab33e1c8139633132cb9eccda0af",
            "name": "Spirit"
        },
        "time": "05:00"
    }
}
```
