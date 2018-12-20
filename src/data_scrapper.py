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
    header = {'Authorization': token}
    r_ranking = requests.get(BASEPATH_API_MPG+'league/'+league+"/ranking", headers=header)
    if r_ranking.ok:
        parsed = json.loads(r_ranking.content.decode('utf-8'))
        return parsed
    else:
        raise NoLeagueException("The league "+league+"doesn't exists")
