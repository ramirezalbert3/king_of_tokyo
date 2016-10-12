coverage erase
coverage run -m unittest discover
coverage report -m dice.py player.py game.py kingAgent.py
