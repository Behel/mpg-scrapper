def get_score(match):
    retour = ""
    team_home = match['data']['teamHome']['name']
    score_home = match['data']['teamHome']['score']
    team_away = match['data']['teamAway']['name']
    score_away = match['data']['teamAway']['score']
    retour += team_home + "   " + str(score_home) + "-" + str(score_away) + "   " + team_away + "\n"

    bonus = match['data']['bonus']
    if not bonus:
        retour += "     Pas de bonus utilisé sur ce match\n"
    else:
        try:
            bonus_home = bonus["home"]
            retour += "     "+team_home+" a utilisé " + get_bonus(bonus_home) + "\n"
        except KeyError:
            pass
        try:
            bonus_away = bonus["away"]
            retour += "     "+team_away+" a utilisé " + get_bonus(bonus_away) + "\n"
        except KeyError:
            pass

    return retour


def get_bonus(json):
    bonuses = {
        1: 'Valise',
        2: 'Zahia',
        3: 'Suarez',
        4: 'Red Bull',
        5: 'Miroir',
        6: 'Chapron',
        7: 'Pat Evra'
    }
    team = {
        1: "à domicile",
        2: "à l'extérieur"
    }

    if json['type']==4:
        return bonuses[json['type']] + " sur " + json['playerName']
    elif json['type']==5:
        return bonuses[json['type']] + " sur " + json['playerName'] + "(équipe " + team[json['team']] + ")"
    else:
        return bonuses[json['type']]


def print_ranking(ranking):
    beautiful_ranking = ""
    for i in range(0, 6):
        ligne = ranking['ranking'][i]
        team = ranking['teams'][ligne['teamid']]['name']
        have_rotaldos = ligne['rotaldo']
        used_bonuses = ligne['bonusUser']
        points = ligne['points']
        played = ligne['played']
        diff = ligne['difference']
        series = ligne['series']
        beautiful_ranking += \
            str(i+1) + " - " +\
            team + " - " +\
            str(points) + "pts (" +\
            str(diff) + ") - " +\
            str(played) + "matches joués - Série : " +\
            series + ". "
        if not have_rotaldos:
            beautiful_ranking += "Toujours pas de Rotaldo pour ce joueur ! "
        if not used_bonuses:
            beautiful_ranking += "Le joueur a encore tous ses bonus pour l'instant... "
        beautiful_ranking += "\n"

    return beautiful_ranking


