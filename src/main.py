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

    leagues = config.get('Leagues', 'leagues_6_players').split(',')
    # Pour l'instant je gère que les ligues de 6 pour la boucle, mais je vais variabiliser ca
    # TODO : Avant l'appel de la boucle, récupérer les infos sur la ligue (nbe de joueurs notamment)
    season = config.get('Leagues', 'season')

    try:
        # Récupération du token de connexion
        token = data_scrapper.get_token(username, pwd)

        # Pour chacune des ligues, je récupère le résultat & je fais un traitement simple dessus
        for league in leagues:
            for day in range(1, 11):
                for match in range(1, 3):
                    try:
                        match = data_scrapper.get_match_summary(token, league, season+"_"+str(day)+"_"+str(match))
                        result = data_intelligence.get_score(match)
                        print(result)

                    except NoMatchException as nme:
                        print(nme.msg)

        # Pour chacune des ligues je récupère le classeent et je printe un résultat simple dessus
        for league in leagues:
            try:
                ranking = data_scrapper.get_ranking(token, league)
                result = data_intelligence.print_ranking(ranking)
                print(result)

            except NoLeagueException as nle:
                print(nle.msg)

    except NoTokenException as nte:
        print(nte.msg)


if __name__ == '__main__':
    main()
