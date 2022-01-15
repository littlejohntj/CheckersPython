def convert(piece):
    if piece == 0:
        return '_'
    elif piece == 1:
        return 'X'
    elif piece == -1:
        return 'O'
    elif piece == -2:
        return 'Q'
    elif piece == 2:
        return 'K'

def print_flat_board(board):
    for i in range(8):
        formated_line = [convert(piece) for piece in board[i*8:(i*8)+8]]
        print(''.join(formated_line))