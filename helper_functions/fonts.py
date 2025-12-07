from helper_functions.globals import *
from helper_functions import globals as g

def drawfont():
  fontObj = pygame.font.Font(None, 32)
  textSurfaceObj = fontObj.render('Hello World!', True, BLACK, WHITE)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (200, 150)
  g.DISPLAYSURF.blit(textSurfaceObj, textRectObj)