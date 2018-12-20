import configparser
import data_scrapper
import data_intelligence
from my_errors import NoTokenException, NoMatchException, NoLeagueException


def main():
    ###############################
    # Récupération des paramètres #
    ###############################

    config = configparser.RawConfigParser()
    config.read('idents.ini')

    username = config.get('Id', 'username')
    pwd = config.get('Id', 'password')

    leagues = config.get('Leagues', 'leagues').split(',')

    try:
        # Récupération du token de connexion
        token = data_scrapper.get_token(username, pwd)

        # Pour chacune des ligues ...
        for league in leagues:

            ### J'affiche le nom de la ligue et je récupère les infos utiles
            league_info = data_scrapper.get_league_info(token, league)

            # Journée en cours (dernière ou à venir)
            current_match_day = data_scrapper.get_calendar(token, league)['data']['results']['currentMatchDay']
            max_match_day = data_scrapper.get_calendar(token, league)['data']['results']['maxMatchDay']

            # Récupération de la saison en cours
            palmares = data_scrapper.get_palmares(token, league)
            if not palmares:
                season = 1
            else:
                season = max(palmares['winners'], key=lambda item: item['season'])['season']+1

            print("----")
            print("Ligue " + league_info['leagueName'] + " | Saison "+str(season))
            print("----")
            print("Résultats autour de la journée " + str(current_match_day)+"/"+str(max_match_day))

            ### Je récupère le résultat des matches & je fais un traitement simple dessus
            no_more_matches = False
            match_number = (int(league_info['players']/2))
            for day in range(1, current_match_day+1):
                print("Journée "+str(day))
                for match in range(1, match_number+1):
                    try:
                        match = data_scrapper.get_match_summary(token, league, str(season)+"_"+str(day)+"_"+str(match))
                        result = data_intelligence.get_score(match)
                        print(result)
                    except NoMatchException:
                        no_more_matches = True
                        break
                if no_more_matches:
                    print("Journée non jouée encore")
                    break

            ### Je récupère le classeent et j'affiche un résultat simple dessus
            try:
                ranking = data_scrapper.get_ranking(token, league)
                result = data_intelligence.print_ranking(ranking)
                print(result)
            except NoLeagueException as nle:
                print(nle.msg)

            ### Je récupère les infos marrantes des stats
            try:
                players_stats = data_scrapper.get_players_stats(token, league)
                print("Le joueur en tête du Petro-green Dollar est " +
                      players_stats["best_petro"][0]['player'] + " (ratio : " +
                      str(players_stats["best_petro"][0]['ratio'])+") pour " +
                      players_stats['teams'][players_stats["best_petro"][0]['teamid']]['name'])
            except NoLeagueException as nle:
                print(nle.msg)

    except NoTokenException as nte:
        print(nte.msg)


if __name__ == '__main__':
    main()
