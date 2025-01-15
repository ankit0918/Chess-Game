import numpy as np

class ChessData:
    bot=""
    game=True
    outline_flag = False
    chess_turn="white"
    active_piece = ""
    outline_moves = []
    chess_board = np.array([
        ['black_rook1', 'black_pawn1', '.', '.', '.', '.', 'white_pawn1', 'white_rook1'],
        ['black_knight1', 'black_pawn2', '.', '.', '.', '.', 'white_pawn2', 'white_knight1'],
        ['black_bishop1', 'black_pawn3', '.', '.', '.', '.', 'white_pawn3', 'white_bishop1'],
        ['black_queen1', 'black_pawn4', '.', '.', '.', '.', 'white_pawn4', 'white_queen1'],
        ['black_king', 'black_pawn5', '.', '.', '.', '.', 'white_pawn5', 'white_king'],
        ['black_bishop2', 'black_pawn6', '.', '.', '.', '.', 'white_pawn6', 'white_bishop2'],
        ['black_knight2', 'black_pawn7', '.', '.', '.', '.', 'white_pawn7', 'white_knight2'],
        ['black_rook2', 'black_pawn8', '.', '.', '.', '.', 'white_pawn8', 'white_rook2']
    ])
    starting_chess_board=np.array([
        ['black_rook1', 'black_pawn1', '.', '.', '.', '.', 'white_pawn1', 'white_rook1'],
        ['black_knight1', 'black_pawn2', '.', '.', '.', '.', 'white_pawn2', 'white_knight1'],
        ['black_bishop1', 'black_pawn3', '.', '.', '.', '.', 'white_pawn3', 'white_bishop1'],
        ['black_queen1', 'black_pawn4', '.', '.', '.', '.', 'white_pawn4', 'white_queen1'],
        ['black_king', 'black_pawn5', '.', '.', '.', '.', 'white_pawn5', 'white_king'],
        ['black_bishop2', 'black_pawn6', '.', '.', '.', '.', 'white_pawn6', 'white_bishop2'],
        ['black_knight2', 'black_pawn7', '.', '.', '.', '.', 'white_pawn7', 'white_knight2'],
        ['black_rook2', 'black_pawn8', '.', '.', '.', '.', 'white_pawn8', 'white_rook2']
    ])
    move_sound=False
    removed_pieces = []
    dragging_flag=False
    castle=""
    has_piece_moved={'black_king':False,'white_king':False,'black_rook2':False,'black_rook1':False,'white_rook1':False,'white_rook2':False}
    player_color=""
    bot_move=[]
    bot_piece=""
    promotion_piece=''
    promotion_location=[]
    en_passant_moves = {'initial': None, 'final': None, 'color': None}
    en_passant_turn = ''


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
    def get_chess_turn(cls):
        return cls.chess_turn
    
    @classmethod
    def update_chess_turn(cls):
        if cls.chess_turn=="white":
            cls.chess_turn="black"
        elif cls.chess_turn=="black": 
            cls.chess_turn="white"

    @classmethod
    def get_removed_piece(cls):
        return cls.removed_pieces
    
    @classmethod
    def update_removed_piece(cls,new_removed_piece):
        if new_removed_piece != '':
            cls.removed_pieces.append(new_removed_piece)
        else:
            cls.removed_pieces = []

    
    @classmethod
    def get_move_sound(cls):
        return cls.move_sound
    
    @classmethod
    def update_move_sound(cls,move_sound_logic):
        cls.move_sound=move_sound_logic

    @classmethod
    def get_dragging_flag(cls):
        return cls.dragging_flag
    
    @classmethod
    def update_dragging_flag(cls,flag_option):
        cls.dragging_flag=flag_option

    @classmethod
    def game_over(cls):
        cls.game=False

    @classmethod
    def get_game(cls):
        return cls.game
    
    @classmethod
    def new_game(cls):
        cls.game =True
    

    
    @classmethod
    def get_has_piece_moved(cls,piece):
        return cls.has_piece_moved[piece]
    
    @classmethod
    def update_has_piece_moved(cls,piece):
        if piece in cls.has_piece_moved:
            cls.has_piece_moved[piece]=True
    @classmethod
    def get_castling_side(cls):
        return cls.castle
    
    @classmethod
    def update_get_castling_side(cls,castle_side):
        cls.castle=castle_side

    @classmethod
    def board_reset(cls):
        cls.chess_board = cls.starting_chess_board.copy()
        cls.chess_turn="white"
        cls.active_piece = ""
        cls.castle=""
        cls.has_piece_moved={'black_king':False,'white_king':False,'black_rook2':False,'black_rook1':False,'white_rook1':False,'white_rook2':False}
    
    @classmethod
    def get_player_color(cls):
        return cls.player_color
    
    @classmethod
    def update_player_color(cls,color):
        cls.player_color=color

    @classmethod
    def get_bot(cls):
        return cls.bot
    
    @classmethod
    def update_bot_level(cls,level):
        cls.bot=level
    
    @classmethod
    def get_bot_move(cls):
        if cls.bot_piece != "" :
            return cls.bot_move,cls.bot_piece
        else:
            return False
    
    @classmethod
    def update_bot_move(cls,move,piece):
        cls.bot_move=move
        cls.bot_piece=piece
        
    @classmethod
    def get_promotion_piece(cls):
        if cls.promotion_piece != "" :
            return cls.promotion_location,cls.promotion_piece
        else:
            return False
    
    @classmethod
    def update_promotion_piece(cls,location,piece):
        cls.promotion_piece = piece
        cls.promotion_location = location
    
    @classmethod
    def update_en_passant_piece(cls, x, y):
        if x != -1 and y != -1:
            if ChessData.get_chess_turn() == "white":
                initial_positions = []
                if x > 1 and "black_pawn" in ChessData.chess_board[x-1][y]:
                    initial_positions.append([x-1, y])  # Use list instead of np.array
                if x < 7 and "black_pawn" in ChessData.chess_board[x+1][y]:
                    initial_positions.append([x+1, y])  # Use list instead of np.array
                if initial_positions:
                    cls.en_passant_moves = {'initial': initial_positions, 'final': [x, y+1], 'color': 'black'}  # Use list instead of np.array
            else:
                initial_positions = []
                if x > 1 and "white_pawn" in ChessData.chess_board[x-1][y]:
                    initial_positions.append([x-1, y])  # Use list instead of np.array
                if x < 7 and "white_pawn" in ChessData.chess_board[x+1][y]:
                    initial_positions.append([x+1, y])  # Use list instead of np.array
                if initial_positions:
                    cls.en_passant_moves = {'initial': initial_positions, 'final': [x, y-1], 'color': 'white'}  # Use list instead of np.array
        else:
            cls.en_passant_moves = {'initial': None, 'final': None, 'color': None}

    @classmethod
    def get_en_passant_piece(cls,update=False):
        if cls.en_passant_moves['initial'] is None:
            return False
        elif ChessData.get_chess_turn() == "white" and cls.en_passant_moves['color'] == "white":
            return cls.en_passant_moves
        elif ChessData.get_chess_turn() == "black" and cls.en_passant_moves['color'] == "black":
            return cls.en_passant_moves
        elif (ChessData.get_chess_turn() == "white" and cls.en_passant_moves['color'] == "black") or (ChessData.get_chess_turn() == "black" and cls.en_passant_moves['color'] == "white") and update:
            ChessData.update_en_passant_piece(-1,-1)
            return False