import requests
from oddsapi.utils import read_txt

# An api key is emailed to you when you sign up to a plan
# Get a free API key at https://api.the-odds-api.com/
API_KEY = read_txt('odds_api_key.txt')

SPORT = 'basketball_nba' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'h2h,spreads' # h2h | spreads | totals. Multiple can be specified if comma delimited

ODDS_FORMAT = 'decimal' # decimal | american

DATE_FORMAT = 'iso' # iso | unix

DAYS_FROM = 1


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# First get a list of in-season sports
#   The sport 'key' from the response can be used to get odds in the next request
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def get_sports(api_key =  read_txt('odds_api_key.txt'), all = True):
    """get_sports

    Args:
        api_key (str, required): your API key. Defaults to read_txt('odds_api_key.txt').
        all (bool, optional): If true, returns all sports. Defaults to True.

    Returns:
        dict:
        [
            {
                "key": "americanfootball_ncaaf",
                "group": "American Football",
                "title": "NCAAF",
                "description": "US College Football",
                "active": true,
                "has_outrights": false
            },
            {
                "key": "americanfootball_nfl",
                "group": "American Football",
                "title": "NFL",
                "description": "US Football",
                "active": true,
                "has_outrights": false
            },
            {
                "key": "americanfootball_nfl_super_bowl_winner",
                "group": "American Football",
                "title": "NFL Super Bowl Winner",
                "description": "Super Bowl Winner 2021/2022",
                "active": true,
                "has_outrights": true
            },
            ...
        ]
    """
    url = 'https://api.the-odds-api.com/v4/sports'
    sports_response = requests.get(url, params={
        'apiKey': api_key,
        'all': str(all).lower() if isinstance(all, bool) else all
    })
    if sports_response.status_code != 200:
        print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')

    else:
        return sports_response.json()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# Now get a list of live & upcoming games for the sport you want, along with odds for different bookmakers
# This will deduct from the usage quota
# The usage quota cost = [number of markets specified] x [number of regions specified]
# For examples of usage quota costs, see https://the-odds-api.com/liveapi/guides/v4/#usage-quota-costs
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def get_sport_odds(sport_key =  SPORT,
                   api_key =  read_txt('odds_api_key.txt'),
                   regions =  REGIONS,
                   markets =  MARKETS,
                   odds_format =  ODDS_FORMAT,
                   date_format =  DATE_FORMAT):
    """get_sport_odds

    Args:
        sport_key (str, optional): sport_key to look up odds for. Defaults to SPORT.
        api_key (str, required): Your API key. Defaults to read_txt('odds_api_key.txt').
        regions (str, optional): uk | us | eu | au. Multiple can be specified if comma delimited. Defaults to REGIONS.
        markets (str, optional): h2h | spreads | totals | outrights. Multiple can be specified if comma delimited. Defaults to MARKETS.
        odds_format (str, optional): decimal | american. Defaults to ODDS_FORMAT.
        date_format (str, optional): iso | unix. Defaults to DATE_FORMAT.

    Returns:
        dict : "bookmakers": [
            {
                "key": "unibet",
                "title": "Unibet",
                "last_update": "2021-06-10T13:33:18Z",
                "markets": [
                    {
                        "key": "h2h",
                        "outcomes": [
                            {
                                "name": "Dallas Cowboys",
                                "price": 240
                            },
                            {
                                "name": "Tampa Bay Buccaneers",
                                "price": -303
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "outcomes": [
                            {
                                "name": "Dallas Cowboys",
                                "price": -109,
                                "point": 6.5
                            },
                            {
                                "name": "Tampa Bay Buccaneers",
                                "price": -111,
                                "point": -6.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "caesars",
                "title": "Caesars",
                "last_update": "2021-06-10T13:33:48Z",
                "markets": [
                    {
                        "key": "h2h",
                        "outcomes": [
                            {
                                "name": "Dallas Cowboys",
                                "price": 240
                            },
                            {
                                "name": "Tampa Bay Buccaneers",
                                "price": -278
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "outcomes": [
                            {
                                "name": "Dallas Cowboys",
                                "price": -110,
                                "point": 6.5
                            },
                            {
                                "name": "Tampa Bay Buccaneers",
                                "price": -110,
                                "point": -6.5
                            }
                        ]
                    }
                ]
            },
            ...
                ]
            }
        ]
    },
...
    """
    url = 'https://api.the-odds-api.com/v4/sports/{}/odds'.format(sport_key)
    sport_response = requests.get(url, params={
        'apiKey': api_key,
        'regions': regions,
        'markets': markets,
        'oddsFormat': odds_format,
        'dateFormat': date_format
    })
    if sport_response.status_code != 200:
        print(f'Failed to get sport odds: status_code {sport_response.status_code}, response body {sport_response.text}')
    else:
        return sport_response.json()


def get_sport_scores(sport_key =  SPORT,
                     api_key = read_txt('odds_api_key.txt'),
                     days_from = DAYS_FROM,
                     date_format = DATE_FORMAT):
    """get_sport_scores

        Args:
            sport_key (str, optional): sport_key to look up odds for. Defaults to SPORT.
            api_key (str, required): Your API key. Defaults to read_txt('odds_api_key.txt').
            days_from (int, optional): Integer from 1 to 3. Defaults to DAYS_FROM.
            date_format (str, optional): iso | unix. Defaults to DATE_FORMAT.

        Returns:
            dict :
            [
                {
                    "id": "572d984e132eddaac3da93e5db332e7e",
                    "sport_key": "basketball_nba",
                    "sport_title": "NBA",
                    "commence_time": "2022-02-06T03:10:38Z",
                    "completed": true,
                    "home_team": "Sacramento Kings",
                    "away_team": "Oklahoma City Thunder",
                    "scores": [
                        {
                            "name": "Sacramento Kings",
                            "score": "113"
                        },
                        {
                            "name": "Oklahoma City Thunder",
                            "score": "103"
                        }
                    ],
                    "last_update": "2022-02-06T05:18:19Z"
                },
                ...
                {
                    "id": "4b25562aa9e87b57aa16f970abaec8cc",
                    "sport_key": "basketball_nba",
                    "sport_title": "NBA",
                    "commence_time": "2022-02-07T02:11:01Z",
                    "completed": false,
                    "home_team": "Los Angeles Clippers",
                    "away_team": "Milwaukee Bucks",
                    "scores": [
                        {
                            "name": "Los Angeles Clippers",
                            "score": "40"
                        },
                        {
                            "name": "Milwaukee Bucks",
                            "score": "37"
                        }
                    ],
                    "last_update": "2022-02-07T02:47:23Z"
                },
                {
                    "id": "19434a586e3723c55cd3d028b90eb112",
                    "sport_key": "basketball_nba",
                    "sport_title": "NBA",
                    "commence_time": "2022-02-08T00:10:00Z",
                    "completed": false,
                    "home_team": "Charlotte Hornets",
                    "away_team": "Toronto Raptors",
                    "scores": null,
                    "last_update": null
                },
            ]
    """
    url = 'https://api.the-odds-api.com/v4/sports/{}/scores'.format(sport_key)
    sport_response = requests.get(url, params={
        'apiKey': api_key,
        'daysFrom': days_from,
        'dateFormat': date_format
    })
    if sport_response.status_code != 200:
        print(f'Failed to get sport odds: status_code {sport_response.status_code}, response body {sport_response.text}')
    else:
        return sport_response.json()

def get_usage(api_key = read_txt('odds_api_key.txt')):
    """get_usage

        Args:
            api_key (str, required): Your API key. Defaults to read_txt('odds_api_key.txt').

        Returns:
            dict :
                {
                    'Remaining requests': 4499996,
                    'Used requests': 4
                }
    """
    url = 'https://api.the-odds-api.com/v4/sports'
    sports_response = requests.get(url, params={
        'api_key': api_key
    })
    if sports_response.status_code != 200:
        print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')

    else:
        # Check the usage quota
        print('Remaining requests', sports_response.headers['x-requests-remaining'])
        print('Used requests', sports_response.headers['x-requests-used'])
        return {
            'Remaining requests': sports_response.headers['x-requests-remaining'],
            'Used requests': sports_response.headers['x-requests-used']
        }
