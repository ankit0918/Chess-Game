import numpy as np

class ChessData:
    outline_flag = False
    chess_turn="white"
    active_piece = ""
    outline_moves = []
    is_first_move= True
    chess_board = np.array([
        ['black_rook1', 'black_pawn1', '.', '.', '.', '.', 'white_pawn1', 'white_rook1'],
        ['black_knight1', 'black_pawn2', '.', '.', '.', '.', 'white_pawn2', 'white_knight1'],
        ['black_bishop1', 'black_pawn3', '.', '.', '.', '.', 'white_pawn3', 'white_bishop1'],
        ['black_queen', 'black_pawn4', '.', '.', '.', '.', 'white_pawn4', 'white_queen'],
        ['black_king', 'black_pawn5', '.', '.', '.', '.', 'white_pawn5', 'white_king'],
        ['black_bishop2', 'black_pawn6', '.', '.', '.', '.', 'white_pawn6', 'white_bishop2'],
        ['black_knight2', 'black_pawn7', '.', '.', '.', '.', 'white_pawn7', 'white_knight2'],
        ['black_rook2', 'black_pawn8', '.', '.', '.', '.', 'white_pawn8', 'white_rook2']
    ])

    @classmethod
    def get_chess_board(cls):
        return cls.chess_board

    @classmethod
    def get_outline_flag(cls):
        return cls.outline_flag

    @classmethod
    def true_outline_flag(cls):
        cls.outline_flag = True  # Toggle the outline flag

    @classmethod
    def false_outline_flag(cls):
        cls.outline_flag = False  # Toggle the outline flag

    @classmethod
    def update_chess_board(cls, new_chess_board):
        cls.chess_board = new_chess_board  # Update the chess board with a new one

    @classmethod
    def get_outline_moves(cls):
        return cls.outline_moves
    
    @classmethod
    def update_outline_moves(cls,new_outline_moves):
        cls.outline_moves= new_outline_moves

    @classmethod
    def get_active_piece(cls):
        return cls.active_piece
    
    @classmethod
    def update_active_piece(cls,new_piece):
        cls.active_piece= new_piece

    @classmethod
    def get_is_first_move(cls):
        return cls.is_first_move
    
    @classmethod
    def update_is_first_move(cls):
        cls.is_first_move =False

    @classmethod
    def get_chess_turn(cls):
        return cls.chess_turn
    
    @classmethod
    def update_chess_turn(cls):
        if cls.chess_turn=="white":
            cls.chess_turn="black"
        elif cls.chess_turn=="black": 
            cls.chess_turn="white"