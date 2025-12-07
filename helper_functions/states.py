from helper_functions.pieces import *
from helper_functions.globals import *

def createplayerstate():
  return joker()

def createenemystate():
  return enemy_team()

def createmovementsets(player):
  return player

def createboardstate():
  board = []
  for i in range (BOARDDEPTH):
    layer = []
    for j in range (BOARDWIDTH):
      surface = []
      for k in range (BOARDHEIGHT):
        space = tile()
        space.i = i
        space.j = j
        space.k = k
        rise = space.rise
        run = space.run
        height = space.height
        space.ltposx = 225 + rise*(k) - rise*j
        space.ltposy = 180 + run*(k) + (run*j - height*i)
        if i != BOARDDEPTH-1:
          space.inactivate()
        surface.append(space)
      layer.append(surface)
    board.append(layer)
  return board