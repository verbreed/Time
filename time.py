import pygame,sys,asyncio
from helper_functions import *
from helper_functions.globals import *
from helper_functions.player.movelists import *
from helper_functions.draw import *
from helper_functions.play import *
from helper_functions.board import *
from helper_functions.states import *
from pygame.locals import *
  
#==========================================================
# STATES
#==========================================================

#============================================
# FONT DEFINITIONS
#============================================

#============================================
# BOARD DEFINITIONS
#============================================

#======================================================================
# PLAYER MOVELISTS
#======================================================================

#===================================================
# PLAY DEFINITIONS
#===================================================

#==================================================================
# MISC.
#==================================================================

#==================================================================
# DRAW DEFINITIONS
#==================================================================

#==========================================================
# SETUP MAIN + MAIN
#==========================================================
async def main():
  running = True
  mousex = 0
  mousey = 0

  pygame.display.set_caption('time')
  player = createplayerstate()
  board = createboardstate()
  enemy_team = createenemystate()
  enemy_team.establishteam()
  player.setuphand(7)
  
  while running:
    pygame.font.init()
    growTimer = pygame.time.get_ticks()
    DISPLAYSURF.fill(WHITE)
    boardtype = 'grassy_plains'
    board = tilereset(board, boardtype)
    player.resethand()
    player = updateplayerdepth(board, player)
    enemy_team = updateenemydepth (board, enemy_team)
    showplayermovelists(board, player, enemy_team)

    for event in pygame.event.get():
      if event.type == QUIT:
        running = False
      elif event.type == MOUSEMOTION:
        mousex, mousey = event.pos
      elif event.type == MOUSEBUTTONUP:
        mousex, mousey = event.pos
        #player = playertakeactionathand(player, mousex, mousey)
        board, player, enemy_team = playertakeactionatpos(board, player, enemy_team, mousex, mousey)

      player = checkforwin(player, enemy_team)
      player = playertakeactionathand(player, mousex, mousey)
      player, enemy_team = enemymove(player, enemy_team)
      board = highlightpos(board, mousex, mousey)
      drawboard(board)
      #for i in range (BOARDDEPTH):
      #  for j in range (BOARDWIDTH):
      #    for k in range (BOARDHEIGHT):
      #      if player.i == i and player.j == j and player.k == k:
      #        x = board[i][j][k].ltposx + 35
      #        y = board[i][j][k].ltposy - player.height
      #        DISPLAYSURF.blit(player.image, (x, y))
      drawpieces(player, enemy_team, board)
      drawhold(player)
      drawhand(player)
      drawtime(player, enemy_team)
      drawturn(player, enemy_team)
      pygame.display.update()
      fpsClock.tick(FPS)
      await asyncio.sleep(0)
  
  pygame.quit()

if __name__ == '__main__':
  asyncio.run(main())