# HLTV Web Scraping API

This project provides a simple API built with Flask that scrapes information from the [HLTV.org](https://www.hltv.org) website. The API allows users to retrieve detailed information about a specific CS2 team based on their team ID and name or an event based on their event ID and name

## Features

The API provides the following information for a given CS2 team:
- **Team Name**
- **Team Logo Image**
- **Player Names and Flags**
- **Valve Ranking**
- **HLTV Ranking**
- **Coach Name and Flag**
- **Team Trophies**
- **Upcoming Matches**
- **Match results**

The API provides the following information for a given CS2 event:
- **Event name**
- **Event date**
- **Prize pool**
- **Number of teams**
- **Event Location**
- **Prize distribution**

## Endpoints

### `GET /team/<team_id>/<team_name>`

This endpoint retrieves detailed information about the team identified by its **team ID** and **team name**.

#### Parameters:
- `team_id` (integer): The ID of the team on HLTV.org.
- `team_name` (string): The name of the team (use the exact team name from the URL on HLTV.org).

#### Example Request:

GET /team/5995/g2

```json
{
    "name": "G2",
    "image": "https://img-cdn.hltv.org/teamlogo/zFLwAELOD15BjJSDMMNBWQ.png?ixlib=java-2.1.0&w=50&s=affb583e6716d8ee904826992255cc4b",
    "players": [
        {
            "nickname": "Snax",
            "flag": "https://www.hltv.org/img/static/flags/30x20/PL.gif",
            "image": "https://img-cdn.hltv.org/playerbodyshot/FMdfl2Ajy3zclnLiBQmsd-.png?ixlib=java-2.1.0&w=400&s=2e5974af64c6f4412c9e7bda15e9fffc",
            "title": "Janusz 'Snax' Pogorzelski"
        },
        {
            "nickname": "NiKo",
            "flag": "https://www.hltv.org/img/static/flags/30x20/BA.gif",
            "image": "https://img-cdn.hltv.org/playerbodyshot/eefPmsiMIo4dAiiPUmZE6-.png?ixlib=java-2.1.0&w=400&s=8d9765f9d2c40c13d7bd6c96c45a2849",
            "title": "Nikola 'NiKo' Kovač"
        },
        {
            "nickname": "huNter-",
            "flag": "https://www.hltv.org/img/static/flags/30x20/BA.gif",
            "image": "https://img-cdn.hltv.org/playerbodyshot/3dH0n73hE5olzCgXPetK_H.png?ixlib=java-2.1.0&w=400&s=77f0dc3e6ca0595afbf0db6c9f7ae0de",
            "title": "Nemanja 'huNter-' Kovač"
        },
        {
            "nickname": "malbsMd",
            "flag": "https://www.hltv.org/img/static/flags/30x20/GT.gif",
            "image": "https://img-cdn.hltv.org/playerbodyshot/ZaIqlLqQQv_3QWrbXCmcQl.png?ixlib=java-2.1.0&w=400&s=2c89cb0010d7e7ca29970e9809e8a82b",
            "title": "Mario 'malbsMd' Samayoa"
        },
        {
            "nickname": "m0NESY",
            "flag": "https://www.hltv.org/img/static/flags/30x20/RU.gif",
            "image": "https://img-cdn.hltv.org/playerbodyshot/F8-kMfRKbV5UDnMo4elY5J.png?ixlib=java-2.1.0&w=400&s=8b740a6d3e55871a8d773b298b486e8c",
            "title": "Ilya 'm0NESY' Osipov"
        }
    ],
    "ranking": {
        "valve_ranking": "#1",
        "hltv_ranking": "#1"
    },
    "coach": {
        "nickname": "TaZ",
        "flag": "https://www.hltv.org/img/static/flags/30x20/PL.gif"
    },
    "trophies": [
        {
            "title": "BLAST Premier World Final 2024",
            "image": "https://img-cdn.hltv.org/eventtrophy/nuo7w87aLUMtHP3fMDrUBy.png?ixlib=java-2.1.0&w=200&s=9b1c3109637232c4025216d0d0b3a7f9",
            "url": "https://www.hltv.org/events/7557/blast-premier-world-final-2024"
        },
        {
            "title": "BLAST Premier Fall Final 2024",
            "image": "https://img-cdn.hltv.org/eventtrophy/k5mryGqAKos7ucHAFgXOpH.png?ixlib=java-2.1.0&w=200&s=26bc9500dbb74e1725b50bebc0fa9057",
            "url": "https://www.hltv.org/events/7556/blast-premier-fall-final-2024"
        },
        {
            "title": "IEM Dallas 2024",
            "image": "https://img-cdn.hltv.org/eventtrophy/KrtnWOzdex1yPlFApI85xh.png?ixlib=java-2.1.0&w=200&s=464fa547b50c24e3cc97cd63bc3677df",
            "url": "https://www.hltv.org/events/7438/iem-dallas-2024"
        },
        {
            "title": "IEM Cologne 2023",
            "image": "https://img-cdn.hltv.org/eventtrophy/AN5DSgQSDDCU4mYDoc2KKH.png?ixlib=java-2.1.0&w=200&s=7668a2fbadcc49789c94aa5fc1ddd2a5",
            "url": "https://www.hltv.org/events/6811/iem-cologne-2023"
        },
        {
            "title": "IEM Katowice 2023",
            "image": "https://img-cdn.hltv.org/eventtrophy/sNjuu3rWTmIS4BFpa6jpS3.png?ixlib=java-2.1.0&w=200&s=897662b715fdc363db1060f2b84014a7",
            "url": "https://www.hltv.org/events/6809/iem-katowice-2023"
        },
        {
            "title": "BLAST Premier World Final 2022",
            "image": "https://img-cdn.hltv.org/eventtrophy/Ea_kuyTOUamLqmDQF8tMyd.png?ixlib=java-2.1.0&w=200&s=1b128f481db40416f2bc5e85b4984a3f",
            "url": "https://www.hltv.org/events/6349/blast-premier-world-final-2022"
        },
        {
            "title": "DreamHack Masters Malmö 2017",
            "image": "/img/static/event/trophies/2684.png",
            "url": "https://www.hltv.org/events/2684/dreamhack-masters-malm-2017"
        },
        {
            "title": "ESL Pro League Season 5 Finals",
            "image": "/img/static/event/trophies/2557.png",
            "url": "https://www.hltv.org/events/2557/esl-pro-league-season-5-finals"
        },
        {
            "title": "DreamHack Open Tours 2017",
            "image": "/img/static/event/trophies/2568.png",
            "url": "https://www.hltv.org/events/2568/dreamhack-open-tours-2017"
        },
        {
            "title": "ECS Season 1 Finals",
            "image": "/img/static/event/trophies/2248.png",
            "url": "https://www.hltv.org/events/2248/ecs-season-1-finals"
        }
    ]
}
```

### `GET /matches/<team_id>/<team_name>`

This endpoint retrieves detailed information about the next matches schedules from team identified by its **team ID** and **team name**.

#### Parameters:
- `team_id` (integer): The ID of the team on HLTV.org.
- `team_name` (string): The name of the team (use the exact team name from the URL on HLTV.org).

#### Example Request:

GET /matches/5995/g2

```json
{
    "match_url": "https://www.hltv.org/matches/2377734/g2-vs-faze-perfect-world-shanghai-major-2024",
    "details": {
        "date": "14 Dec",
        "time": "10:00",
        "team1": {
            "name": "G2",
            "logo": "https://img-cdn.hltv.org/teamlogo/zFLwAELOD15BjJSDMMNBWQ.png?ixlib=java-2.1.0&w=100&s=88aeba1564bc27de69fb2302e47e1a7c"
        },
        "team2": {
            "name": "FaZe",
            "logo": "https://img-cdn.hltv.org/teamlogo/zbcwVqDX-cVjB7EidzNoPd.png?ixlib=java-2.1.0&w=100&s=5d6488f42991807e0d921d0290c711ab"
        },
        "match_format": "Best of 3 (LAN)"
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
    "title": "Perfect World Shanghai Major 2024",
    "date": "Dec 5th - Dec 15th 2024",
    "prize_pool": "$1,250,000",
    "teams": "16",
    "location": {
        "flag": "https://www.hltv.org/img/static/flags/30x20/CN.gif",
        "location": "Shanghai, China",
        "type": "Unknown"
    },
    "prize_distribution": {
        "1st": [
            {
                "team_name": "Spirit",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/syrtYYKR7sBRw3ZHy1YFX7.png?ixlib=java-2.1.0&w=200&s=155e7cf96a2271f213fd06d9c3dd163b",
                "prizes": [
                    "$500,000"
                ]
            }
        ],
        "2nd": [
            {
                "team_name": "FaZe",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/zbcwVqDX-cVjB7EidzNoPd.png?ixlib=java-2.1.0&w=200&s=d2a74b1f21c671ce247ca94cee323c7d",
                "prizes": [
                    "$170,000"
                ]
            }
        ],
        "3-4th": [
            {
                "team_name": "G2",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/zFLwAELOD15BjJSDMMNBWQ.png?ixlib=java-2.1.0&w=200&s=457c1663356d6dd20e39a1188b267802",
                "prizes": [
                    "$80,000"
                ]
            },
            {
                "team_name": "MOUZ",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/IejtXpquZnE8KqYPB1LNKw.svg?ixlib=java-2.1.0&s=7fd33b8def053fbfd8fdbb58e3bdcd3c",
                "prizes": [
                    "$80,000"
                ]
            }
        ],
        "5-8th": [
            {
                "team_name": "Vitality",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/ogcHrcCdzRvxbYvAz04KAN.png?ixlib=java-2.1.0&w=200&s=df5ace7c0551382453806466a214b606",
                "prizes": [
                    "$45,000"
                ]
            },
            {
                "team_name": "HEROIC",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/4S22uk_gnZTiQiI-hhH4yp.png?ixlib=java-2.1.0&w=200&s=f8e7b7825d7a6989479f1773574c9fd5",
                "prizes": [
                    "$45,000"
                ]
            },
            {
                "team_name": "Liquid",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/JMeLLbWKCIEJrmfPaqOz4O.svg?ixlib=java-2.1.0&s=c02caf90234d3a3ebac074c84ba1ea62",
                "prizes": [
                    "$45,000"
                ]
            },
            {
                "team_name": "The MongolZ",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/bRk2sh_tSTO6fq1GLhgcal.png?ixlib=java-2.1.0&w=200&s=d82e930fcea873b51ceab34c1a338b02",
                "prizes": [
                    "$45,000"
                ]
            }
        ],
        "9-11th": [
            {
                "team_name": "FURIA",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/mvNQc4csFGtxXk5guAh8m1.svg?ixlib=java-2.1.0&s=11e5056829ad5d6c06c5961bbe76d20c",
                "prizes": [
                    "$20,000"
                ]
            },
            {
                "team_name": "Natus Vincere",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/9iMirAi7ArBLNU8p3kqUTZ.svg?ixlib=java-2.1.0&s=4dd8635be16122656093ae9884675d0c",
                "prizes": [
                    "$20,000"
                ]
            },
            {
                "team_name": "MIBR",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/sVnH-oAf1J5TnMwoY4cxUC.png?ixlib=java-2.1.0&w=200&s=50d17f716e2c25219327e061a4ac046d",
                "prizes": [
                    "$20,000"
                ]
            }
        ],
        "12-14th": [
            {
                "team_name": "paiN",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/iUUCFwCOFmOrwhB8q8smMg.svg?ixlib=java-2.1.0&s=1446e1cf3d02deb8190fe6efd14e4ce4",
                "prizes": [
                    "$20,000"
                ]
            },
            {
                "team_name": "GamerLegion",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/jS__cj2F09Bl8qBU_CvkQR.png?ixlib=java-2.1.0&w=200&s=9b9252b6e3737f4a32c1de457bc308ce",
                "prizes": [
                    "$20,000"
                ]
            },
            {
                "team_name": "3DMAX",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/QGPDS3Z2-aMXwCYVgA4RWH.png?ixlib=java-2.1.0&w=200&s=7ee780a2a85e9a27098df617b87fb702",
                "prizes": [
                    "$20,000"
                ]
            }
        ],
        "15-16th": [
            {
                "team_name": "BIG",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/OgMRQA35hopXA8kDwMFHIY.svg?ixlib=java-2.1.0&s=ec7bc44165c7acf4224a22a1338ab7d7",
                "prizes": [
                    "$20,000"
                ]
            },
            {
                "team_name": "Wildcard",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/-46lJ-DcmPL_j_5R2WvLiS.png?ixlib=java-2.1.0&w=200&s=c668203646759ca9af0549d6ea1fb93f",
                "prizes": [
                    "$20,000"
                ]
            }
        ]
    }
}
```

GET events/8172/cct-season-2-europe-series-15

```json
{
    "title": "CCT Season 2 Europe Series 15",
    "date": "Dec 3rd - Dec 15th 2024",
    "prize_pool": "$50,000",
    "teams": "24",
    "location": {
        "flag": "https://www.hltv.org/img/static/flags/30x20/EU.gif",
        "location": "Europe",
        "type": "Online"
    },
    "prize_distribution": {
        "1st": [
            {
                "team_name": "Spirit Academy",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/txUq00aBKY7O4fLVJegmi_.png?ixlib=java-2.1.0&w=200&s=e844936f7a1bb7e5dad4d2380ccda958",
                "prizes": [
                    "$22,000"
                ]
            }
        ],
        "2nd": [
            {
                "team_name": "ECSTATIC",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/yx_pWjWbW-2F5oF5nLHXc8.png?ixlib=java-2.1.0&w=200&s=5ccdd3ba666603e7bdec3ff5f54c946c",
                "prizes": [
                    "$10,000"
                ]
            }
        ],
        "3-4th": [
            {
                "team_name": "ENCE",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/-X8NoyWC_1gYqUHvZqcpkc.svg?ixlib=java-2.1.0&s=85bb9daa6f846fa097c5942f2565fdb8",
                "prizes": [
                    "$5,000"
                ]
            },
            {
                "team_name": "9INE",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/BGC4LXlC8s4W0xWyelk2BI.png?ixlib=java-2.1.0&w=200&s=be93217172852a964de706d720f4e2cc",
                "prizes": [
                    "$5,000"
                ]
            }
        ],
        "5-8th": [
            {
                "team_name": "AMKAL",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/KNl9ZeR2afmpj3-J0fSilz.png?ixlib=java-2.1.0&w=200&s=0a43afad15e8ed5e080afbd3e9ce2524",
                "prizes": [
                    "$2,000"
                ]
            },
            {
                "team_name": "Metizport",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/uHxM4VRz0qIDKVsckVrbjv.png?ixlib=java-2.1.0&w=200&s=c1902727f945c44a4c0199bc524e73b4",
                "prizes": [
                    "$2,000"
                ]
            },
            {
                "team_name": "Zero Tenacity",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/5RRO6-Yzo13W3OjXINCQEJ.png?ixlib=java-2.1.0&w=200&s=3a68f9dbaebe9e20d9ca71d80120ebaa",
                "prizes": [
                    "$2,000"
                ]
            },
            {
                "team_name": "Aurora Young Blud",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/oEbMpT1GK1wi2A3H_hRi06.png?ixlib=java-2.1.0&w=200&s=c8fcdd9ce555349ca6303bf15bdf8253",
                "prizes": [
                    "$2,000"
                ]
            }
        ],
        "9-16th": [
            {
                "team_name": "Into the Breach",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/Tgyea9TVbc37YisEY4Y13a.png?ixlib=java-2.1.0&w=200&s=06c157edc8f8e6017bb74883a415f256",
                "prizes": []
            },
            {
                "team_name": "ALTERNATE aTTaX",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/JoPCUmjz0PcCiCPqNHIyR3.svg?ixlib=java-2.1.0&s=24f23b651e49eaab76bae4945b19d7ec",
                "prizes": []
            },
            {
                "team_name": "Monte",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/2tc9n4fHkiRIX2FiJSkhgt.png?ixlib=java-2.1.0&w=200&s=52c60e51e8c1797c3101eb339cdf0d24",
                "prizes": []
            },
            {
                "team_name": "SINNERS",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/9l_WdQSU9JsNHzpK-pwOG2.svg?ixlib=java-2.1.0&s=af432c3ef61c0c843331cc0dc2fed1ed",
                "prizes": []
            },
            {
                "team_name": "DMS",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/8CHmYIq6FPDGeRSWzFX1uu.png?ixlib=java-2.1.0&w=200&s=82a76e54671f7547c60d39a8349384d9",
                "prizes": []
            },
            {
                "team_name": "GUN5",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/h7rPBXKkg9rmhbeBVmRG28.png?ixlib=java-2.1.0&w=200&s=a5887bf2774a83a1cc9deaae7a9f46db",
                "prizes": []
            },
            {
                "team_name": "Endpoint",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/LrJW0lI8ifto6tzTjNkxpw.png?ixlib=java-2.1.0&w=200&s=2e00c6f11eb400463fcef4f8a2287acf",
                "prizes": []
            },
            {
                "team_name": "B8",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/O6nRWTCjUzBAR4pcOcrpSG.png?ixlib=java-2.1.0&w=200&s=7c49777d91e3f2b8de8dbe439f8fb112",
                "prizes": []
            }
        ],
        "17-19th": [
            {
                "team_name": "KOI",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/lPfoQHMaORhkfTpcbR-lCQ.png?ixlib=java-2.1.0&w=200&s=1a398c9c33156ada6eb2b8c9513015f5",
                "prizes": []
            },
            {
                "team_name": "Fire Flux",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/dEkPG3QFLGo6xl9DtGPsm2.png?ixlib=java-2.1.0&w=200&s=232673008b529ffec63bb1252d8107c8",
                "prizes": []
            },
            {
                "team_name": "Insilio",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/_xqicJ8DEOBw-M74mVqh2-.png?ixlib=java-2.1.0&w=200&s=8f660b6eed5612a4d2732212029ab782",
                "prizes": []
            }
        ],
        "20-22nd": [
            {
                "team_name": "CYBERSHOKE",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/MDFborrTXebGid2bmaTA2B.png?ixlib=java-2.1.0&w=200&s=3a10ec70e137a72a9015ea4e2c68ecc5",
                "prizes": []
            },
            {
                "team_name": "FAVBET",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/4on2ywp0wcfk7vjUN3OjZk.png?ixlib=java-2.1.0&w=200&s=80ec7a319df779f5be5853fca66f0cfa",
                "prizes": []
            },
            {
                "team_name": "FLuffy Gangsters",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/1rM-qNVqKfIbsfOQp7bjTq.png?ixlib=java-2.1.0&w=200&s=c469664f76f1a1a55f60e4053b60cfc9",
                "prizes": []
            }
        ],
        "23-24th": [
            {
                "team_name": "Sampi",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/f8LhN1SIFHyICHa1OjVmvx.png?ixlib=java-2.1.0&w=200&s=2246c4f3d780ec708a7ebf439a21eba6",
                "prizes": []
            },
            {
                "team_name": "Gaimin Gladiators",
                "team_logo": "https://img-cdn.hltv.org/teamlogo/nnUUng-EKdho6MRIhK3-5N.png?ixlib=java-2.1.0&w=200&s=b13fa4ef8b8ed3c7971404ec2f5f8738",
                "prizes": []
            }
        ]
    }
}
```

### `GET /result/<match_id>/<match_name>`

This endpoint retrieves detailed information about a completed match, including team results and map details, identified by its **match ID** and **match name**.

#### Parameters:
- `match_id` (integer): The unique ID of the match on HLTV.org. This value can be found in the match's URL.
- `match_name` (string): The specific name of the match (use the exact match name from the URL on HLTV.org).

#### Example Request:

GET /result/2377734/g2-vs-faze-perfect-world-shanghai-major-2024

```json
{
    "details": {
        "date": "14 Dec",
        "time": "11:35",
        "team1": {
            "name": "G2",
            "logo": "https://img-cdn.hltv.org/teamlogo/zFLwAELOD15BjJSDMMNBWQ.png?ixlib=java-2.1.0&w=100&s=88aeba1564bc27de69fb2302e47e1a7c"
        },
        "team2": {
            "name": "FaZe",
            "logo": "https://img-cdn.hltv.org/teamlogo/zbcwVqDX-cVjB7EidzNoPd.png?ixlib=java-2.1.0&w=100&s=5d6488f42991807e0d921d0290c711ab"
        },
        "match_format": "Best of 3 (LAN)"
    },
    "maps": [
        {
            "map": "Ancient",
            "team1_score": "6",
            "team2_score": "13"
        },
        {
            "map": "Nuke",
            "team1_score": "14",
            "team2_score": "16"
        },
        {
            "map": "Anubis",
            "team1_score": "-",
            "team2_score": "-"
        }
    ]
}
```