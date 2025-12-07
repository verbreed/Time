import random
from helper_functions.globals import *

def randomizeboardactivity(board):
  for i in range (BOARDDEPTH):
    for j in range (BOARDWIDTH):
      for k in range (BOARDHEIGHT):
        board[i][j][k].active = random.choice([0,1])
  return board