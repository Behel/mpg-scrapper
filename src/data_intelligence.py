def get_score(match):
    team_home = match['data']['teamHome']['name']
    score_home = match['data']['teamHome']['score']
    team_away = match['data']['teamAway']['name']
    score_away = match['data']['teamAway']['score']
    return team_home + "   " + str(score_home) + "-" + str(score_away) + "   " + team_away


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
        if have_rotaldos:
            beautiful_ranking += "Toujours pas de Rotaldo pour ce joueur ! "
        if not used_bonuses:
            beautiful_ranking += "Le joueur a encore tous ses bonus pour l'instant... "
        beautiful_ranking += "\n"

    return beautiful_ranking


