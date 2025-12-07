import random
from helper_functions.globals import *
from helper_functions.pieces import *
from timer import *

def checkforwin(player, enemy):
  if len(enemy.enemylist) == 0:
    player.haswon = 1
  return player

def checktake(player, enemy):
  if player.istaken == 0:
    for piece in range (len(enemy.enemylist)):
      if player.j == enemy.enemylist[piece].j and player.k == enemy.enemylist[piece].k:
        if player.isturn == 1:
          enemy.enemylist[piece].istaken = 1
          player.holdlist.append(enemy.enemylist[piece].type)
          enemy.deletemember(piece)
          return player, enemy
        elif player.isturn == 0:
          player.holdlist.append(10)
          player.istaken = 1
          return player, enemy
    return player, enemy
            
def playertakeactionatpos(board, player, enemy, x, y):
  for i in range (BOARDDEPTH):
    for j in range (BOARDWIDTH):
      for k in range (BOARDHEIGHT):
        if player.isturn == 1:
          if x > board[i][j][k].ltposx + 6 and x < board[i][j][k].ltposx + board[i][j][k].pixlength - 6:
            if y > board[i][j][k].ltposy + 6 and y < board[i][j][k].ltposy + board[i][j][k].pixwidth - 3:
              for move in range (len(player.movelist)):
                if board[i][j][k].i == player.movelist[move].i:
                  if board[i][j][k].j == player.movelist[move].j and board[i][j][k].k == player.movelist[move].k:
                    player.i = i
                    player.j = j
                    player.k = k
                    #board = attackboard(board, player.i, player.j, player.k, 8)                    
                    player, enemy = checktake(player, enemy)
                    player.isturn = 0
                    player.turntimer.checktimer()
                    player.timetotal = player.turntimer.timeelapsed + player.timetotal
                    player.turntimer = None
                    enemy.turntimer = settimer()
                    player.enemypausetimer = settimer()
                    return board, player, enemy
              #for move in range (len(player.bishopmovelist)):
              #  if board[i][j][k].i == player.bishopmovelist[move].i:
              #    if board[i][j][k].j == player.bishopmovelist[move].j and board[i][j][k].k == player.bishopmovelist[move].k:
              #      player.i = i
              #      player.j = j
              #      player.k = k
              #      player, enemy = checktake(player, enemy)
              #      player.isturn = 0
              #      player.turntimer.checktimer()
              #      player.timetotal = player.turntimer.timeelapsed + player.timetotal
              #      player.turntimer = None
              #      enemy.turntimer = settimer()
              #      player.enemypausetimer = settimer()
              #      return board, player, enemy
  return board, player, enemy

def playertakeactionathand(player, x, y):
  for move in range (len(player.handlist)): 
    if move == len(player.handlist):
      if x > player.handlist[move].ltposx and x < player.handlist[move].ltposx + player.handlist[move].run:
        if y > player.handlist[move].lyposy and y < player.handlist[move].ltposy + player.handlist[move].rise:
          player.handlist[move].ltposy = player.handlist[move].ltposy - player.handlist[move].rise
          pygame.transform.scale2x(player.handlist[move].image)
          return player
    else:
      if x > player.handlist[move].ltposx and x < player.handlist[move].ltposx + player.handlist[move].ltposx:
        if y > player.handlist[move].ltposy and y < player.handlist[move].ltposy + player.handlist[move].rise:
          player.handlist[move].ltposy = player.handlist[move].ltposy - player.handlist[move].rise
          player.handlist[move].image = pygame.transform.scale2x(player.handlist[move].image)
          return player
  return player

def enemymove(player, enemy):
  if enemy.enemylist:
    if player.isturn == 0:
      player.enemypausetimer.checktimer()
      if player.enemypausetimer.timeelapsed >= 1250:
        for index in range (len(enemy.enemylist)):
          if player.j == enemy.enemylist[index].j and player.k - 1 == enemy.enemylist[index].k or player.j - 1 == enemy.enemylist[index].j and player.k + 1 == enemy.enemylist[index].k:
            enemy.enemylist[index].j = player.j
            enemy.enemylist[index].k = player.k
            checktake(player, enemy)
            player.isturn = 1
            player.turntimer = settimer()
            enemy.turntimer.checktimer()
            enemy.timetotal = enemy.turntimer.timeelapsed + enemy.timetotal
            player.enemypausetimer = None
            enemy.turntimer = None
            return player, enemy
        if len(enemy.enemylist) > 0:
          rand = random.randrange(0, (len(enemy.enemylist)))
          if enemy.enemylist[rand].j <= BOARDWIDTH - 2 and enemy.enemylist[rand].j + 1 != player.j and enemy.enemylist[rand].k != player.k:
            if enemy.enemylist[rand].type == 1:
              enemy.enemylist[rand].j = enemy.enemylist[rand].j + 1
              player.isturn = 1
              player.turntimer = settimer()
              enemy.turntimer.checktimer()
              enemy.timetotal = enemy.turntimer.timeelapsed + enemy.timetotal
              player.enemypausetimer = None
              enemy.turntimer = None
            #elif enemy.enemylist[rand].type == 2:
              #
            return player, enemy
        elif len(enemy.enemylist) == 0:
          enemy.enemylist[0].j = enemy.enemylist[0].j + 1
          changetoplayerturn(player, enemy)
          return player, enemy
      if player.enemypausetimer.timeelapsed >= 12500:
        changetoplayerturn(player, enemy)
        return player, enemy
  enemy = checktransform(enemy)
  return player, enemy

def changetoplayerturn (player, enemy):
  player.isturn = 1
  player.turntimer = settimer()
  enemy.turntimer.checktimer()
  enemy.total = enemy.turntimer.timeelapsed + enemy.timetotal
  player.enemypausetimer = None
  enemy.turntimer = None
  return player, enemy

def checktransform (enemy):
  for i in range (len(enemy.enemylist)):
    if enemy.enemylist[i].j == 7:
      add = enemy_queen()
      add.i = enemy.enemylist[i].i
      add.j = enemy.enemylist[i].j
      add.k = enemy.enemylist[i].k
      del enemy.enemylist [i]
      enemy.enemylist.insert(i, add)
  return enemy       

def updateplayerdepth(board, player):
  i = player.i
  j = player.j
  k = player.k
  if board[i][j][k].active == 0:
    for new in range (BOARDDEPTH):
      if board[new][j][k].active == 1:
        player.i = new
  return player

def updateenemydepth(board, enemy):
  for index in range (len(enemy.enemylist)):
    i = enemy.enemylist[index].i
    j = enemy.enemylist[index].j
    k = enemy.enemylist[index].k
    if board[i][j][k].active == 0:
      for new in range (BOARDDEPTH):
       if board[new][j][k].active == 1:
          enemy.enemylist[index].i = new
  return enemy

def attackboard(board, i, j, k, limit):
  if board[i][j][k].active == 1 and i-2 > 0:
    board[i][j][k].active = 0
    board[i-1][j][k].active = 1
    if k-1 < limit and i-1 > 0 and k-1 > 0:
      if board[i][j][k-1].active == 1:
        board[i][j][k-1].active = 0
        board[i-1][j][k-1].active = 1
    if k+1 < limit and i-1 > 0:
      if board[i][j][k+1].active == 1:
        board[i][j][k+1].active = 0
        board[i-1][j][k+1].active = 1
    if j-1 < limit and i-1 > 0 and j-1 > 0:
      if board[i][j-1][k].active == 1:
        board[i][j-1][k].active = 0
        board[i-1][j-1][k].active = 1
    if j+1 < limit and i-1 > 0:
      if board[i][j+1][k].active == 1:
        board[i][j+1][k].active = 0
        board[i-1][j+1][k].active = 1
  return board