import requests
import json
from my_errors import NoTokenException, NoMatchException, NoLeagueException

##############
# Constantes #
##############

BASEPATH_API_MPG = "https://api.monpetitgazon.com/"
ENDPOINT_LOGIN = "user/signIn"


def get_token(username, password):
    payload = {'email': username, 'password': password, 'language': "fr-FR"}
    r = requests.post(BASEPATH_API_MPG+ENDPOINT_LOGIN, data=payload)
    if r.ok:
        parsed = json.loads(r.content.decode('utf-8'))
        return parsed['token']
    else:
        raise NoTokenException("Can't have the Token ...")


def get_match_summary(token, league, match):
    header = {'Authorization': token}
    r_summary = requests.get(BASEPATH_API_MPG+'league/'+league+"/results/"+match, headers=header)
    if r_summary.ok:
        parsed = json.loads(r_summary.content.decode('utf-8'))
        return parsed
    else:
        raise NoMatchException("The match "+match+" (league: "+league+") has not been played")


def get_ranking(token, league):
    return __get_league_page(token, league, "ranking")


def get_players_stats(token, league):
    return __get_league_page(token, league, "ranking/player")


def get_team_stats(token, league):
    return __get_league_page(token, league, "ranking/team")


def get_bonus_stats(token, league):
    return __get_league_page(token, league, "ranking/bonus")


def get_palmares(token, league):
    return __get_league_page(token, league, "ranking/winners")


def get_teamplayers(token, league):
    return __get_league_page(token, league, "teams")


def get_league_info(token, league):
    return __get_league_page(token, league, "status")


def get_calendar(token, league):
    return __get_league_page(token, league, "calendar")


def __get_league_page(token, league, page):
    header = {'Authorization': token}
    r_league = requests.get(BASEPATH_API_MPG+'league/'+league+"/"+page, headers=header)
    if r_league.ok:
        parsed = json.loads(r_league.content.decode('utf-8'))
        return parsed
    else:
        raise NoLeagueException("The league "+league+" doesn't exists")
