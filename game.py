import numpy as np
from cmath import pi
from error import MultiplePiecesBlockPath, NoDirectionSpecified, NoPieceAtIndex, NoPiecesOnBoard, PieceMovedInncorrectly, PieceMovedOutOfBounds, PlayerMovedOutOfTurn, SpaceBlockedByCurrentUser, TriedToMoveSomeoneElsesPiece, TriedToMoveTooManyTimes
from player import Player

class Game:

    def __init__(self, player_one, player_two):
        self.board = self.make_flat_board()
        self.player_one = player_one
        self.player_two = player_two
        self.current_player = self.player_one
        self.completed = False
        self.winner = None

    def flip_current_player(self):
        if self.current_player.user == self.player_one.user:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one
    
    def board_index(self, row, col):
        return (row * 8) + col

    def check_winner(self):

        self.player_one_piece_count = 0
        self.player_two_piece_count = 0

        for piece in self.board:
            if piece < 0:
                self.player_one_piece_count += 1
            elif piece > 0:
                self.player_two_piece_count += 1
        
        if self.player_one_piece_count == 0 and self.player_two_piece_count == 0:
            raise NoPiecesOnBoard

        if self.player_one_piece_count == 0:
            self.winner = self.player_two
            self.completed = True
        elif self.player_two_piece_count == 0:
            self.winner = self.player_one
            self.completed = True

    def move_piece(self, row, col, direction_list, player):

        if len(direction_list) == 0:
            raise NoDirectionSpecified

        if self.board[ self.board_index(row, col) ] == 0:
            raise NoPieceAtIndex

        user = player.user
        
        if self.board[ self.board_index(row, col) ] != user and self.board_index(row, col) != user * 2:
            raise TriedToMoveSomeoneElsesPiece

        if self.current_player.user != user:
            raise PlayerMovedOutOfTurn

        jumped_pieces = []
        new_row = row
        new_col = col

        for direction in direction_list:

            if self.board[ self.board_index(new_row, new_col) ] == -1 and ( direction == 'dr' or direction == 'dl' ):
                raise PieceMovedInncorrectly

            if self.board[ self.board_index(new_row, new_col) ] == 1 and ( direction == 'ur' or direction == 'ul' ):
                raise PieceMovedInncorrectly

            row_modifier = 0
            col_modifier = 0

            if direction == 'ur':
                row_modifier = -1
                col_modifier = 1
            elif direction == 'ul':
                row_modifier = -1
                col_modifier = -1
            elif direction == 'dr':
                row_modifier = 1
                col_modifier = 1
            elif direction == 'dl':
                row_modifier = 1
                col_modifier = -1

            if new_row + row_modifier > 7 or new_row + row_modifier < 0 or new_col + col_modifier < 0 or new_col + col_modifier > 7:
                raise PieceMovedOutOfBounds
        
            new_row = new_row + row_modifier
            new_col = new_col + col_modifier
        
            if self.board[ self.board_index(new_row, new_col) ] == user:
                raise SpaceBlockedByCurrentUser
        
            if self.board[ self.board_index(new_row, new_col) ] == user * -1:
                
                # possible jump situation
            
                if new_row + row_modifier < 0 or new_row + row_modifier > 7 or new_col + col_modifier < 0 or new_col + col_modifier > 7:
                    raise PieceMovedOutOfBounds
                
                self.board[ self.board_index(new_row + row_modifier, new_col + col_modifier) ]
                if self.board[ self.board_index(new_row + row_modifier, new_col + col_modifier) ] != 0:
                    raise MultiplePiecesBlockPath
                
                jumped_pieces.append( (new_row, new_col) )
                
                new_row = new_row + row_modifier
                new_col = new_col + col_modifier

        # validate jumps
        if len(direction_list) > 1 and len(jumped_pieces) != len(direction_list):
            raise TriedToMoveTooManyTimes
            
        if user == -1:
            if new_row == 0:
                self.board[ self.board_index(new_row, new_col) ] = -2
            else:
                self.board[ self.board_index(new_row, new_col) ] = self.board[ self.board_index(row, col) ]
        elif user == 1:
            if new_row == 7:
                self.board[ self.board_index(new_row, new_col) ] = 2
            else:
                self.board[ self.board_index(new_row, new_col) ] = self.board[ self.board_index(row, col) ]

        self.board[ self.board_index(row, col) ] = 0
        for piece in jumped_pieces:
            self.board[ self.board_index(piece[0], piece[1]) ] = 0
        self.flip_current_player()

    def make_flat_board(self):
        board = np.zeros(64)
        for i in range(8):
            for j in range(8):
                if i < 3 and ( (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1) ):
                    board[ (i * 8) + j ] = 1
                elif i > 4 and ( (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1) ):
                    board[ (i * 8) + j ] = -1
        return board