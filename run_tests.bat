coverage erase
coverage run -m unittest discover
coverage report -m dice.py player.py agent.py kingAgent.py
