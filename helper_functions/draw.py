from helper_functions.globals import *
from helper_functions.activitylist import *

def drawboard(board):
  #if growTimer <= 2000:
  #  DISPLAYSURF.blit(tileIMG_0, (x - (22*i), y + (6*i)))
  #elif growTimer > 2000 and growTimer <= 6000:
  #  DISPLAYSURF.blit(tileIMG_1, (x - (22*i), y + (6*i)))
  #elif growTimer > 6000 and growTimer <= 14000:
  #  DISPLAYSURF.blit(tileIMG_2, (x - (22*i), y + (6*i)))
  #elif growTimer > 14000:
  #  DISPLAYSURF.blit(tileIMG_3, (x - (22*i), y + (6*i)))
  activitylist = createactivitylist(board)
  activitylist = sortheightactivitylist(activitylist)
  for i in range (ACTIVELIST):
    DISPLAYSURF.blit(player_hold_bar, (0, 25))
    DISPLAYSURF.blit(player_hold_bar, (0, 425))
    DISPLAYSURF.blit(activitylist[i].image, (activitylist[i].ltposx, activitylist[i].ltposy))

def drawpieces(player, enemy, board):
  for i in range (BOARDDEPTH):
    for j in range (BOARDWIDTH):
      for k in range (BOARDHEIGHT):
        for piece in range (len(enemy.enemylist)):
          if enemy.enemylist[piece].istaken == 0: 
            if enemy.enemylist[piece].i == i and enemy.enemylist[piece].j == j and enemy.enemylist[piece].k == k:
              x = board[i][j][k].ltposx + 16
              y = board[i][j][k].ltposy - enemy.enemylist[piece].height
              DISPLAYSURF.blit(enemy.enemylist[piece].image, (x, y))
        if player.istaken == 0:
          if player.i == i and player.j == j and player.k == k:
            x = board[i][j][k].ltposx + 14
            y = board[i][j][k].ltposy - player.height
            DISPLAYSURF.blit(player.image, (x, y))
  player.clearmovelist()

def drawhold(player):
  for i in range (len(player.holdlist)):
    if  player.holdlist[i] == 1:
      DISPLAYSURF.blit(enemy_pawn_IMG, (10 + 35*i, 20))
    elif player.holdlist[i] == 2:
      DISPLAYSURF.blit(enemy_queen_IMG, (10 + 35*i, 15))
    elif player.holdlist[i] == 10:
      DISPLAYSURF.blit(joker_IMG, (10 + 35*i, 20))

def drawhand(player):
  for i in range (len(player.handlist)):
    if  player.handlist[i].card_id == 1:
      DISPLAYSURF.blit(player.handlist[i].image, (player.handlist[i].ltposx, player.handlist[i].ltposy))

def drawturn(player, enemy):
  if player.haswon == 1:
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Clear!', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (250, 100)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
  elif player.isturn == 0:
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Opponent', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (250, 100)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
  elif player.isturn == 1:
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Player', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (250, 100)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
  elif player.istaken == 1:
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Loss!', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (250, 100)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

def drawtime(player, enemy):
  nullvalue = 0
  
  if player.istaken == 1:
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    textSurfaceObjPlayerTurn = fontObj.render('%20d s.' % (nullvalue), True, BLACK, WHITE)
    textSurfaceObjPlayerTotal = fontObj.render('%20d s.' % (player.timetotal/1000), True, BLACK, WHITE)
    textSurfaceObjEnemyTurn = fontObj.render('%20d s.' % (nullvalue), True, BLACK, WHITE)
    textSurfaceObjEnemyTotal = fontObj.render('%20d s.' % (enemy.timetotal/1000), True, BLACK, WHITE)
    
    textRectObjPlayerTurn = textSurfaceObjPlayerTurn.get_rect()
    textRectObjPlayerTotal = textSurfaceObjPlayerTotal.get_rect()
    textRectObjEnemyTurn = textSurfaceObjEnemyTurn.get_rect()
    textRectObjEnemyTotal = textSurfaceObjEnemyTotal.get_rect()
    
    textRectObjPlayerTurn.center = (100, 105)
    textRectObjPlayerTotal.center = (100, 85)
    textRectObjEnemyTurn.center = (325, 105)
    textRectObjEnemyTotal.center = (325, 85)
    
    DISPLAYSURF.blit(textSurfaceObjPlayerTurn, textRectObjPlayerTurn)
    DISPLAYSURF.blit(textSurfaceObjPlayerTotal, textRectObjPlayerTotal)
    DISPLAYSURF.blit(textSurfaceObjEnemyTurn, textRectObjEnemyTurn)
    DISPLAYSURF.blit(textSurfaceObjEnemyTotal, textRectObjEnemyTotal)
    
  elif player.turntimer:
    
    player.turntimer.checktimer()
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    textSurfaceObjPlayerTurn = fontObj.render('%20d s.' % (player.turntimer.timeelapsed/1000), True, BLACK, WHITE)
    textSurfaceObjPlayerTotal = fontObj.render('%20d s.' % (player.timetotal/1000), True, BLACK, WHITE)
    textSurfaceObjEnemyTurn = fontObj.render('%20d s.' % (nullvalue), True, BLACK, WHITE)
    textSurfaceObjEnemyTotal = fontObj.render('%20d s.' % (enemy.timetotal/1000), True, BLACK, WHITE)
    
    textRectObjPlayerTurn = textSurfaceObjPlayerTurn.get_rect()
    textRectObjPlayerTotal = textSurfaceObjPlayerTotal.get_rect()
    textRectObjEnemyTurn = textSurfaceObjEnemyTurn.get_rect()
    textRectObjEnemyTotal = textSurfaceObjEnemyTotal.get_rect()
    
    textRectObjPlayerTurn.center = (100, 105)
    textRectObjPlayerTotal.center = (100, 85)
    textRectObjEnemyTurn.center = (325, 105)
    textRectObjEnemyTotal.center = (325, 85)
    
    DISPLAYSURF.blit(textSurfaceObjPlayerTurn, textRectObjPlayerTurn)
    DISPLAYSURF.blit(textSurfaceObjPlayerTotal, textRectObjPlayerTotal)
    DISPLAYSURF.blit(textSurfaceObjEnemyTurn, textRectObjEnemyTurn)
    DISPLAYSURF.blit(textSurfaceObjEnemyTotal, textRectObjEnemyTotal)
    
  elif enemy.turntimer and player.isturn == 0:
    
    enemy.turntimer.checktimer()
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    textSurfaceObjPlayerTurn = fontObj.render('%20d s.' % (nullvalue), True, BLACK, WHITE)
    textSurfaceObjPlayerTotal = fontObj.render('%20d s.' % (player.timetotal/1000), True, BLACK, WHITE)
    textSurfaceObjEnemyTurn = fontObj.render('%20d s.' % (enemy.turntimer.timeelapsed/1000), True, BLACK, WHITE)
    textSurfaceObjEnemyTotal = fontObj.render('%20d s.' % (enemy.timetotal/1000), True, BLACK, WHITE)
    
    textRectObjPlayerTurn = textSurfaceObjPlayerTurn.get_rect()
    textRectObjPlayerTotal = textSurfaceObjPlayerTotal.get_rect()
    textRectObjEnemyTurn = textSurfaceObjEnemyTurn.get_rect()
    textRectObjEnemyTotal = textSurfaceObjEnemyTotal.get_rect()
    
    textRectObjPlayerTurn.center = (100, 105)
    textRectObjPlayerTotal.center = (100, 85)
    textRectObjEnemyTurn.center = (325, 105)
    textRectObjEnemyTotal.center = (325, 85)
    
    DISPLAYSURF.blit(textSurfaceObjPlayerTurn, textRectObjPlayerTurn)
    DISPLAYSURF.blit(textSurfaceObjPlayerTotal, textRectObjPlayerTotal)
    DISPLAYSURF.blit(textSurfaceObjEnemyTurn, textRectObjEnemyTurn)
    DISPLAYSURF.blit(textSurfaceObjEnemyTotal, textRectObjEnemyTotal)