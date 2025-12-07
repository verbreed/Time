from helper_functions.globals import *

def drawfont():
  fontObj = pygame.font.Font('freesansbold.ttf', 32)
  textSurfaceObj = fontObj.render('Hello World!', True, BLACK, WHITE)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (200, 150)
  DISPLAYSURF.blit(textSurfaceObj, textRectObj)