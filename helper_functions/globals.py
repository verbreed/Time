import pygame,sys
from pathlib import Path

#============================================================
# INITIALIZING
#============================================================
FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((500, 500))
time = pygame.time.Clock()

BOARDWIDTH  = 8
BOARDHEIGHT = 8
BOARDDEPTH  = 2
ACTIVELIST  = BOARDWIDTH*BOARDHEIGHT

#         R    G     B
WHITE = (255, 255,  255)
BLACK = (  0,   0,    0)

'''
OPPONENT_TURN                     = 'turn_opponent.png'
PLAYER_TURN                       = 'turn_player.png'
JOKER_HOLDER                      = 'joker_holder.png'
ENEMY_QUEEN                       = 'enemy_queen.png'
ENEMY_PAWN                        = 'enemy_pawn.png'

TANK_BASIC                        = 'ground_hex_frame_Tank_stg0.png'

HOLD_BAR                          = 'holding_bar.png'
GROUND_HEX_FRAME_OPTION_STG0      = 'ground_hex_frame_shade_option_stg0.png'
GROUND_HEX_FRAME_HIGHLIGHT_STG0   = 'ground_hex_frame_shade_highlight_stg0.png'
GROUND_HEX_GRASSY_PLAIN           = 'ground_hex_frame_grassy_plains.png'
GROUND_HEX_FRAME_STG0             = 'ground_hex_frame_shade_stg0.png'
GROUND_TILE_FRAME_STG1            = 'ground_tile_frame_stg1.png'
GROUND_TILE_FRAME_STG2            = 'ground_tile_frame_stg2.png'
GROUND_TILE_FRAME_STG3            = 'ground_tile_frame_stg3.png'

#============================================================
# BATTLE CARDS
#============================================================
CARD_FRAME                        = 'card_frame.png' 
CARD_PASS                         = 'card_pass.png'
'''
#============================================================
# FUNCTIONS TO GENERATE GLOBALS
#============================================================
def get_image_path(filename):
    if sys.platform == 'emscripten':
        return f'assets/{filename}'
    else:
        return Path(__file__).parent.parent / 'assets' / filename

globals_images_dict = {
    'turn_opponent'     :'turn_opponent.png',
    'turn_player'       :'turn_player.png',
    'joker_IMG'         :'joker_holder.png',
    'enemy_queen_IMG'   :'enemy_queen.png',
    'enemy_pawn_IMG'    :'enemy_pawn.png',
    'Tank_IMG_BASIC'    :'ground_hex_frame_Tank_stg0.png',
    'player_hold_bar'   :'holding_bar.png',
    'tileOP_0'          :'ground_hex_frame_shade_option_stg0.png',
    'tileHI_0'          :'ground_hex_frame_shade_highlight_stg0.png',
    'tileIMG_0'         :'ground_hex_frame_shade_stg0.png',
    'hexGrassyIMG_0'    :'ground_hex_frame_grassy_plains.png',
    'tileIMG_1'         :'ground_tile_frame_stg1.png',
    'tileIMG_2'         :'ground_tile_frame_stg2.png',
    'tileIMG_3'         :'ground_tile_frame_stg3.png',
    'card_frame'        :'card_frame.png',
    'card_pass'         :'card_pass.png',
}
for var, filename in globals_images_dict.items():
    globals()[var] = pygame.image.load(get_image_path(filename))

'''
#============================================================
# INITIALIZING
#============================================================
turn_opponent   = pygame.image.load(get_image_path(OPPONENT_TURN))
turn_player     = pygame.image.load(get_image_path(PLAYER_TURN))
enemy_queen_IMG = pygame.image.load(get_image_path(ENEMY_QUEEN))
enemy_pawn_IMG  = pygame.image.load(get_image_path(ENEMY_PAWN))

Tank_IMG_BASIC  = pygame.image.load(get_image_path(TANK_BASIC))

player_hold_bar = pygame.image.load(get_image_path(HOLD_BAR))
tileOP_0        = pygame.image.load(get_image_path(GROUND_HEX_FRAME_OPTION_STG0))
tileHI_0        = pygame.image.load(get_image_path(GROUND_HEX_FRAME_HIGHLIGHT_STG0))
tileIMG_0       = pygame.image.load(get_image_path(GROUND_HEX_FRAME_STG0))
hexGrassyIMG_0  = pygame.image.load(get_image_path(GROUND_HEX_GRASSY_PLAIN))
tileIMG_1       = pygame.image.load(get_image_path(GROUND_TILE_FRAME_STG1))
tileIMG_2       = pygame.image.load(get_image_path(GROUND_TILE_FRAME_STG2))
tileIMG_3       = pygame.image.load(get_image_path(GROUND_TILE_FRAME_STG3))

#=============================================================
# BATTLE CARDS
#=============================================================
card_frame      = pygame.image.load(CARD_FRAME)
card_pass       = pygame.image.load(CARD_PASS)
'''