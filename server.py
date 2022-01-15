from game import Game
from error import *

class Server:
    def __init__(self):
        self.games = []

    def make_game(self, player_one, player_two):

        current_game = self.find_game(player_one, player_two)

        if current_game is not None:
            raise OnGoingGameExists

        new_game = Game(player_one, player_two)
        self.games.append(new_game)

    def find_game(self, player_one, player_two):
        for game in self.games:
            if game.player_one.uuid == player_one.uuid and game.player_two.uuid == player_two.uuid:
                return game

    def find_game_critical(self, player_one, player_two):
        for game in self.games:
            if game.player_one.uuid == player_one.uuid and game.player_two.uuid == player_two.uuid:
                return game
        raise NoGameExists

    def move_piece(self, game, row, col, direction_list, player):

        if game.completed:
            raise GameCompleted

        game.move_piece(row, col, direction_list, player)