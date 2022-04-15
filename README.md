# **`oddsapi`**
To access the API, get a free API key from https://the-odds-api.com

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
git clone https://github.com/saiemgilani/oddsapi
cd oddsapi
pip install -e .
```


Then import the package:
```python
import oddsapi 
```


## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from oddsapi.utils import read_txt
from oddsapi.api import *
import argparse
import requests
import pandas as pd


# An api key is emailed to you when you sign up to a plan
# Get a free API key at https://api.the-odds-api.com/
API_KEY = read_txt('odds_api_key.txt')

SPORT = 'basketball_nba' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'h2h,spreads' # h2h | spreads | totals | outrights. Multiple can be specified if comma delimited

ODDS_FORMAT = 'decimal' # decimal | american

DATE_FORMAT = 'iso' # iso | unix

DAYS_FROM = 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# First get a list of in-season sports
#   The sport 'key' from the response can be used to get odds in the next request
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
sports_df = pd.json_normalize(get_sports(api_key =  read_txt('odds_api_key.txt')))
sports_df.to_csv('static/odds_api_sports.csv', index=False)
print(sports_df.head())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# Now get a list of live & upcoming games for the sport you want, along with odds for different bookmakers
# This will deduct from the usage quota
# The usage quota cost = [number of markets specified] x [number of regions specified]
# For examples of usage quota costs, see https://the-odds-api.com/liveapi/guides/v4/#usage-quota-costs
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
get_sport_odds(sport_key =  SPORT,
                   api_key =  read_txt('odds_api_key.txt'),
                   regions =  REGIONS,
                   markets =  MARKETS,
                   odds_format =  ODDS_FORMAT,
                   date_format =  DATE_FORMAT)

get_sport_scores(sport_key =  SPORT,
                     api_key = read_txt('odds_api_key.txt'),
                     days_from = DAYS_FROM,
                     date_format = DATE_FORMAT)

get_usage(api_key = read_txt('odds_api_key.txt'))
```

