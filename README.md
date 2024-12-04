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
        "flag": "/img/static/flags/30x20/BR.gif",
        "name": "sidde"
    },
    "hltv_ranking": "#8",
    "image": "https://img-cdn.hltv.org/teamlogo/mvNQc4csFGtxXk5guAh8m1.svg?ixlib=java-2.1.0&s=11e5056829ad5d6c06c5961bbe76d20c",
    "name": "FURIA",
    "players": [
        {
            "flag": "/img/static/flags/30x20/BR.gif",
            "nickname": "FalleN"
        },
        {
            "flag": "/img/static/flags/30x20/BR.gif",
            "nickname": "chelo"
        },
        {
            "flag": "/img/static/flags/30x20/BR.gif",
            "nickname": "yuurih"
        },
        {
            "flag": "/img/static/flags/30x20/BR.gif",
            "nickname": "KSCERATO"
        },
        {
            "flag": "/img/static/flags/30x20/BR.gif",
            "nickname": "skullz"
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
