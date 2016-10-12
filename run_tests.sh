coverage erase
echo "Running unit tests"
coverage run -m unittest discover
echo -e "\nCoverage report"
coverage report -m dice.py player.py game.py kingAgent.py