from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        self.url = url
    
    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players

class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader.get_players()
        

    def top_scorers_by_nationality(self, nationality):
        top = []
        for player in self.player_reader:
            if player.nationality == nationality:
                top.append(player)

        return top