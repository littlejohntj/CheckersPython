class Error(Exception):
    """Base class for other exceptions"""
    pass

class GameCompleted(Error):
    """Raised when a game has already been completed"""
    pass

class OnGoingGameExists(Error):
    """Raised when a new game is trying to be created but one already exists"""
    pass

class NoGameExists(Error):
    """Raised when a game was expected to exist but it did not"""
    pass

class NoPiecesOnBoard(Error):
    """Raised when there are no pieces left on the board, this should not happen"""
    pass

class NoPieceAtIndex(Error):
    """Raised when there is no piece at the index requested to move"""
    pass

class TriedToMoveSomeoneElsesPiece(Error):
    """Raised when a user tries to move a piece they dont own"""
    pass

class PlayerMovedOutOfTurn(Error):
    """Raised when a player tries to move when it's not their turn"""
    pass

class PieceMovedInncorrectly(Error):
    """Raised when a piece is moved in a direction it is not able to"""
    pass

class PieceMovedOutOfBounds(Error):
    """Raised whjen a piece is moved out of bounds"""
    pass

class SpaceBlockedByCurrentUser(Error):
    """Raised when a user tried to move into a space that is occupied by their own piece"""
    pass

class NoDirectionSpecified(Error):
    """Raised when there was no direction input for a move"""
    pass

class MultiplePiecesBlockPath(Error):
    """Raised when a piece tries to move in a direction where multiple pieces are blocking"""
    pass

class TriedToMoveTooManyTimes(Error):
    """Raised when a piece tries to move that it is allowed to"""
    pass