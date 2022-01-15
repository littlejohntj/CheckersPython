from cmath import pi
from http import server
import numpy as np
from error import TriedToMoveTooManyTimes
from game import Game
from player import Player
from server import Server
from utility import *

server = Server()

player_one = Player(-1, 'abcd')
player_two = Player(1, 'apple')

server.make_game(player_one, player_two)
game = server.find_game_critical(player_one, player_two)

try:
    server.move_piece(game, 5, 0, ['ur', 'ur'], player_one)
    print_flat_board(game.board)
except TriedToMoveTooManyTimes:
    print('player tried to move too many times')

'''
King Double Jump

move_piece(5, 0, ['ur'], -1)
move_piece(2, 1, ['dr'], 1)
move_piece(5, 2, ['ur'], -1)
move_piece(3, 2, ['dl'], 1)
move_piece(6, 3, ['ul'], -1)
move_piece(2, 7, ['dl'], 1)
move_piece(7, 2, ['ur'], -1)
move_piece(5, 0, ['dr'], 1)
move_piece(5, 4, ['ur'], -1)
move_piece(7, 2, ['ur'], 1)
move_piece(7, 0, ['ur'], -1)
move_piece(5, 4, ['ul'], 1)
move_piece(5, 2, ['ur'], -1)
move_piece(3, 2, ['ul'], 1)
move_piece(4, 3, ['ul'], -1)
move_piece(6, 1, ['ur'], -1)
move_piece(2, 1, ['dr', 'dl'], 1)

'''