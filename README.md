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

### `GET /events/<event_id>/<event_name>`

This endpoint retrieves detailed information about an event identified by its **event ID** and **event name**.

#### Parameters:
- `event_id` (integer): The ID of the event on HLTV.org.
- `event_name` (string): The name of the event (use the exact event name from the URL on HLTV.org).

#### Example Request:

GET /events/7524/perfect-world-shanghai-major-2024

```json
{
    "date": "Dec 5th - Dec 15th 2024",
    "location": {
        "flag": "https://www.hltv.org/img/static/flags/30x20/CN.gif",
        "location": "Shanghai, China",
        "type": "Unknown"
    },
    "prize_distribution": {
        "12-14th": [
            {
                "prizes": [
                    "$20,000"
                ],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/iUUCFwCOFmOrwhB8q8smMg.svg?ixlib=java-2.1.0&s=1446e1cf3d02deb8190fe6efd14e4ce4",
                "team_name": "paiN"
            },
            {
                "prizes": [
                    "$20,000"
                ],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/jS__cj2F09Bl8qBU_CvkQR.png?ixlib=java-2.1.0&w=200&s=9b9252b6e3737f4a32c1de457bc308ce",
                "team_name": "GamerLegion"
            },
            {
                "prizes": [
                    "$20,000"
                ],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/QGPDS3Z2-aMXwCYVgA4RWH.png?ixlib=java-2.1.0&w=200&s=7ee780a2a85e9a27098df617b87fb702",
                "team_name": "3DMAX"
            }
        ],
        "15-16th": [
            {
                "prizes": [
                    "$20,000"
                ],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/OgMRQA35hopXA8kDwMFHIY.svg?ixlib=java-2.1.0&s=ec7bc44165c7acf4224a22a1338ab7d7",
                "team_name": "BIG"
            },
            {
                "prizes": [
                    "$20,000"
                ],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/-46lJ-DcmPL_j_5R2WvLiS.png?ixlib=java-2.1.0&w=200&s=c668203646759ca9af0549d6ea1fb93f",
                "team_name": "Wildcard"
            }
        ],
        "1st": [
            {
                "prizes": [
                    "$500,000"
                ]
            }
        ],
        "2nd": [
            {
                "prizes": [
                    "$170,000"
                ]
            }
        ],
        "3-4th": [
            {
                "prizes": [
                    "$80,000"
                ]
            },
            {
                "prizes": [
                    "$80,000"
                ]
            }
        ],
        "5-8th": [
            {
                "prizes": [
                    "$45,000"
                ]
            },
            {
                "prizes": [
                    "$45,000"
                ]
            },
            {
                "prizes": [
                    "$45,000"
                ],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/JMeLLbWKCIEJrmfPaqOz4O.svg?ixlib=java-2.1.0&s=c02caf90234d3a3ebac074c84ba1ea62",
                "team_name": "Liquid"
            },
            {
                "prizes": [
                    "$45,000"
                ],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/bRk2sh_tSTO6fq1GLhgcal.png?ixlib=java-2.1.0&w=200&s=d82e930fcea873b51ceab34c1a338b02",
                "team_name": "The MongolZ"
            }
        ],
        "9-11th": [
            {
                "prizes": [
                    "$20,000"
                ],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/mvNQc4csFGtxXk5guAh8m1.svg?ixlib=java-2.1.0&s=11e5056829ad5d6c06c5961bbe76d20c",
                "team_name": "FURIA"
            },
            {
                "prizes": [
                    "$20,000"
                ],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/9iMirAi7ArBLNU8p3kqUTZ.svg?ixlib=java-2.1.0&s=4dd8635be16122656093ae9884675d0c",
                "team_name": "Natus Vincere"
            },
            {
                "prizes": [
                    "$20,000"
                ],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/sVnH-oAf1J5TnMwoY4cxUC.png?ixlib=java-2.1.0&w=200&s=50d17f716e2c25219327e061a4ac046d",
                "team_name": "MIBR"
            }
        ]
    },
    "prize_pool": "$1,250,000",
    "teams": "16",
    "title": "Perfect World Shanghai Major 2024"
}
```

GET events/8172/cct-season-2-europe-series-15

```json
{
    "date": "Dec 3rd - Dec 15th 2024",
    "location": {
        "flag": "https://www.hltv.org/img/static/flags/30x20/EU.gif",
        "location": "Europe",
        "type": "Online"
    },
    "prize_distribution": {
        "17-19th": [
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/lPfoQHMaORhkfTpcbR-lCQ.png?ixlib=java-2.1.0&w=200&s=1a398c9c33156ada6eb2b8c9513015f5",
                "team_name": "KOI"
            },
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/dEkPG3QFLGo6xl9DtGPsm2.png?ixlib=java-2.1.0&w=200&s=232673008b529ffec63bb1252d8107c8",
                "team_name": "Fire Flux"
            },
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/_xqicJ8DEOBw-M74mVqh2-.png?ixlib=java-2.1.0&w=200&s=8f660b6eed5612a4d2732212029ab782",
                "team_name": "Insilio"
            }
        ],
        "1st": [
            {
                "prizes": [
                    "$22,000"
                ]
            }
        ],
        "20-22nd": [
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/MDFborrTXebGid2bmaTA2B.png?ixlib=java-2.1.0&w=200&s=3a10ec70e137a72a9015ea4e2c68ecc5",
                "team_name": "CYBERSHOKE"
            },
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/4on2ywp0wcfk7vjUN3OjZk.png?ixlib=java-2.1.0&w=200&s=80ec7a319df779f5be5853fca66f0cfa",
                "team_name": "FAVBET"
            },
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/1rM-qNVqKfIbsfOQp7bjTq.png?ixlib=java-2.1.0&w=200&s=c469664f76f1a1a55f60e4053b60cfc9",
                "team_name": "FLuffy Gangsters"
            }
        ],
        "23-24th": [
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/f8LhN1SIFHyICHa1OjVmvx.png?ixlib=java-2.1.0&w=200&s=2246c4f3d780ec708a7ebf439a21eba6",
                "team_name": "Sampi"
            },
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/nnUUng-EKdho6MRIhK3-5N.png?ixlib=java-2.1.0&w=200&s=b13fa4ef8b8ed3c7971404ec2f5f8738",
                "team_name": "Gaimin Gladiators"
            }
        ],
        "2nd": [
            {
                "prizes": [
                    "$10,000"
                ]
            }
        ],
        "3-4th": [
            {
                "prizes": [
                    "$5,000"
                ]
            },
            {
                "prizes": [
                    "$5,000"
                ]
            }
        ],
        "5-8th": [
            {
                "prizes": [
                    "$2,000"
                ]
            },
            {
                "prizes": [
                    "$2,000"
                ]
            },
            {
                "prizes": [
                    "$2,000"
                ]
            },
            {
                "prizes": [
                    "$2,000"
                ]
            }
        ],
        "9-16th": [
            {
                "prizes": []
            },
            {
                "prizes": []
            },
            {
                "prizes": []
            },
            {
                "prizes": []
            },
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/8CHmYIq6FPDGeRSWzFX1uu.png?ixlib=java-2.1.0&w=200&s=82a76e54671f7547c60d39a8349384d9",
                "team_name": "DMS"
            },
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/h7rPBXKkg9rmhbeBVmRG28.png?ixlib=java-2.1.0&w=200&s=a5887bf2774a83a1cc9deaae7a9f46db",
                "team_name": "GUN5"
            },
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/LrJW0lI8ifto6tzTjNkxpw.png?ixlib=java-2.1.0&w=200&s=2e00c6f11eb400463fcef4f8a2287acf",
                "team_name": "Endpoint"
            },
            {
                "prizes": [],
                "team_logo": "https://img-cdn.hltv.org/teamlogo/O6nRWTCjUzBAR4pcOcrpSG.png?ixlib=java-2.1.0&w=200&s=7c49777d91e3f2b8de8dbe439f8fb112",
                "team_name": "B8"
            }
        ]
    },
    "prize_pool": "$50,000",
    "teams": "24",
    "title": "CCT Season 2 Europe Series 15"
}
```