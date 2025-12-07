from helper_functions.globals import *

def tilereset(board, boardtype):
  for i in range(BOARDDEPTH):
    for j in range (BOARDWIDTH):
      for k in range (BOARDHEIGHT):
        if boardtype == 'grassy_plains':
          board[i][j][k].image = hexGrassyIMG_0
        else:
          board[i][j][k].image = tileIMG_0
  return board

def highlightpos(board, x, y):
  for i in range (BOARDDEPTH):
    for j in range (BOARDWIDTH):
      for k in range (BOARDHEIGHT):
        if x > board[i][j][k].ltposx + 6 and x < board[i][j][k].ltposx + board[i][j][k].pixlength - 6:
          if y > board[i][j][k].ltposy + 6 and y < board[i][j][k].ltposy + board[i][j][k].pixwidth - 3:
            board[i][j][k].image = tileHI_0
  return board
