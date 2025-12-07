from helper_functions.globals import *

def showknightmovement(board, player, enemy):
  j = player.j
  k = player.k
  for i in range (BOARDDEPTH):
    if player.istaken == 0:
        if j-2 >= 0 and k-1 >= 0:
          if board [i][j-2][k-1].active == 1:
            board[i][j-2][k-1].image = tileOP_0
            player.movelist.append(board[i][j-2][k-1])
        if j+2 < 8 and k-1 >= 0:
          if board [i][j+2][k-1].active == 1:
            board[i][j+2][k-1].image = tileOP_0
            player.movelist.append(board[i][j+2][k-1])
        if j+2 < 8 and k+1 < 8:
          if board [i][j+2][k+1].active == 1:
            board[i][j+2][k+1].image = tileOP_0
            player.movelist.append(board[i][j+2][k+1])
        if j-2 >= 0 and k+1 < 8:
          if board [i][j-2][k+1].active == 1:
            board[i][j-2][k+1].image = tileOP_0
            player.movelist.append(board[i][j-2][k+1])
        if j-1 >= 0 and k-2 >= 0:
          if board [i][j-1][k-2].active == 1:
            board[i][j-1][k-2].image = tileOP_0
            player.movelist.append(board[i][j-1][k-2])
        if j+1 < 8 and k-2 >= 0:
          if board [i][j+1][k-2].active == 1:
            board[i][j+1][k-2].image = tileOP_0
            player.movelist.append(board[i][j+1][k-2])
        if j+1 < 8 and k+2 < 8:
          if board [i][j+1][k+2].active == 1:
            board[i][j+1][k+2].image = tileOP_0
            player.movelist.append(board[i][j+1][k+2])
        if j-1 >= 0 and k+2 < 8:
          if board [i][j-1][k+2].active == 1:
            board[i][j-1][k+2].image = tileOP_0
            player.movelist.append(board[i][j-1][k+2])
  return board, player
    

def showbishopmovement(board, player, enemy):
  j = player.j
  k = player.k
  for i in range (BOARDDEPTH):
    if player.istaken == 0:
      player.cansee = 1
      for move in range (1,8):
        if j-move >= 0 and k+move < 8 and player.cansee == 1:
            if board[i][j-move][k+move].active == 1 and player.cansee == 1: 
              board[i][j-move][k+move].image = tileOP_0
              player.movelist.append(board[i][j-move][k+move])
              for e in range (len(enemy.enemylist)):
                if j-move == enemy.enemylist[e].j and k+move == enemy.enemylist[e].k:
                  player.cansee = 0
      player.cansee = 1            
      for move in range (1,8):            
        if k-move >= 0 and player.cansee == 1:
            if board[i][j][k-move].active == 1:
               board[i][j][k-move].image = tileOP_0
               player.movelist.append(board[i][j][k-move])
               for e in range (len(enemy.enemylist)):
                if j == enemy.enemylist[e].j and k-move == enemy.enemylist[e].k:
                  player.cansee = 0
      player.cansee = 1
      for move in range (1,8):
        if j+move < 8 and player.cansee == 1:
            if board[i][j+move][k].active == 1:
               board[i][j+move][k].image = tileOP_0
               player.movelist.append(board[i][j+move][k])
               for e in range (len(enemy.enemylist)):
                if j+move == enemy.enemylist[e].j and k == enemy.enemylist[e].k:
                  player.cansee = 0
      #player.cansee = 1         
      #for move in range (1,8):         
      #  if j+move < 8 and k-move >= 0 and player.cansee == 1:
      #    if board[i][j+move][k-move].active == 1:
      #       board[i][j+move][k-move].image = tileOP_0
      #       player.bishopmovelist.append(board[i][j+move][k-move])
      #       for e in range (len(enemy.enemylist)):
      #          if j+move == enemy.enemylist[e].j and k-move == enemy.enemylist[e].k:
      #            player.cansee = 0
  return board, player

def showreversebishopmovement(board, player, enemy):
  j = player.j
  k = player.k
  for i in range (BOARDDEPTH):
    if player.istaken == 0:
      player.cansee = 1
      for move in range (1,8):
        if j+move < 8 and k-move >= 0 and player.cansee == 1:
            if board[i][j+move][k-move].active == 1 and player.cansee == 1: 
              board[i][j+move][k-move].image = tileOP_0
              player.movelist.append(board[i][j+move][k-move])
              for e in range (len(enemy.enemylist)):
                if j+move == enemy.enemylist[e].j and k-move == enemy.enemylist[e].k:
                  player.cansee = 0
      player.cansee = 1            
      for move in range (1,8):            
        if k+move < 8 and player.cansee == 1:
            if board[i][j][k+move].active == 1:
               board[i][j][k+move].image = tileOP_0
               player.movelist.append(board[i][j][k+move])
               for e in range (len(enemy.enemylist)):
                if j == enemy.enemylist[e].j and k+move == enemy.enemylist[e].k:
                  player.cansee = 0
      player.cansee = 1
      for move in range (1,8):
        if j-move >= 0 and player.cansee == 1:
            if board[i][j-move][k].active == 1:
               board[i][j-move][k].image = tileOP_0
               player.movelist.append(board[i][j-move][k])
               for e in range (len(enemy.enemylist)):
                if j-move == enemy.enemylist[e].j and k == enemy.enemylist[e].k:
                  player.cansee = 0
      #player.cansee = 1         
      #for move in range (1,8):         
      #  if j+move < 8 and k-move >= 0 and player.cansee == 1:
      #    if board[i][j+move][k-move].active == 1:
      #       board[i][j+move][k-move].image = tileOP_0
      #       player.bishopmovelist.append(board[i][j+move][k-move])
      #       for e in range (len(enemy.enemylist)):
      #          if j+move == enemy.enemylist[e].j and k-move == enemy.enemylist[e].k:
      #            player.cansee = 0
  player.cansee = 1
  return board, player

def showplayermovelists(board, player, enemy):
    #board, player = showknightmovement(board, player, enemy)
    board, player = showbishopmovement(board, player, enemy)
    board, player = showreversebishopmovement(board, player, enemy)
    return board, player, enemy