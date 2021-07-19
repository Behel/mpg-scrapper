# Deprecated project
Not usable anymore with the shutdown of the website

# MPG Scrapper

Pour lancer MPG Scrapper : 
- ``pip install requirements.txt`` (la baz, tmtc)
- Renommer ``idents.ini.default`` en  ``idents.ini`` 
- Indiquer dans ce fichier son email & mot de passe de connexion à MPG + les identifiants des ligues requêtées. 
- Lancer la commande ``python3 src/main.py`` depuis le dossier mpg-scrapper
- Bim ca affiche les résultats des matches et le classement

Pour l'instant ca affiche des infos sur les matches et le classement, mais à vous de modifier la partie data_intelligence pour retourner ce que vous voulez ! (Stats des joueurs, ...)
