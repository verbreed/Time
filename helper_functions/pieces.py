import random
from helper_functions.globals import *
from pygame.locals import *
from helper_functions.knickknack import *
from time import *

#========================================
# Class Declarations
#========================================

class enemy_team:
	def __init__(self):
		self.enemylist = []
		self.turntimer = None
		self.timetotal = 0
	def establishteam(self):
		#self.enemylist.append(enemy_queen())
		#self.enemylist[0].j = 0
		#self.enemylist[0].k = 3

		# add enemy types to a list for placement
		enemy_type_list = []
		enemy_type_list.append(enemy_pawn)
		#enemy_type_list.append(tank)
		print(enemy_type_list)

		for i in range (5):
		  self.enemylist.append(random.choice(enemy_type_list)())
		  self.enemylist[i].j = random.randint(0,7)
		  self.enemylist[i].k = random.randint(0,7)
		print(self.enemylist)
	def deletemember(self, piece):
		self.enemylist.pop(piece)

class card:
	def __init__(self):
		self.card_id = 0
		self.ind_id = 0
		self.rise = 71
		self.run = 55
		self.ltposx = 0
		self.ltposy = 0
		self.image = card_frame
	def __init__(self, ID):
		if ID == 1:
			self.card_id = 1
			self.ind_id = 0
			self.rise = 71
			self.run = 55
			self.ltposx = 0
			self.ltposy = 0
			self.image = card_pass
	def ResetCard(self, ID):
		if ID == 1:
			self.image = card_pass

class tile:
  def __init__(self):
    self.i = 0
    self.j = 0
    self.k = 0
    self.rise = 28
    self.run = 14
    self.height = 2
    self.ltposx = 0
    self.ltposy = 0
    self.pixlength = 45
    self.pixwidth = 24
    self.image = tileIMG_0
    self.active = 1
  def inactivate(self):
    self.active = 0

class board:
  def __init__(self):
    self.board = []
    self.activitylist = []

class joker:
  def __init__(self):
    self.istaken = 0
    self.movelist = []
    self.holdlist = []
    self.handlist = []
    self.teamlist = []
    self.handsize = 0
    self.cansee = 0
    self.isturn = 1
    self.height = 30
    self.i = 0
    self.j = 4
    self.k = 3
    self.image = joker_IMG
    self.haswon = 0
    self.enemypausetimer = None
    self.turntimer = settimer()
    self.timetotal = 0
  def clearmovelist(self):
    I = set()
    for i in range(len(self.movelist)):
        I.add(i)
    for i in sorted(I, reverse=True):
        del self.movelist[i]
  def clearhandlist(self):
    I = set()
    for i in range(len(self.handlist)):
        I.add(i)
    for i in sorted(I, reverse=True):
        del self.handlist[i]
  def setuphand(self, starthand):
    for i in range (starthand):
      self.handlist.append(card(1))
      self.handlist[i].ltposx = 10 + 35*i
      self.handlist[i].ltposy = 400
  def resethand(self):
    for i in range (len(self.handlist)):
      self.handlist[i].ResetCard(self.handlist[i].card_id)
      self.handlist[i].ltposy = 400
  #def clearknightmovelist(self):
  #  I = set()
  #  for i in range(len(self.knightmovelist)):
  #      I.add(i)
  #  for i in sorted(I, reverse=True):
  #      del self.knightmovelist[i]
  
class enemy_queen:
	def __init__(self):
		self.istaken = 0
		self.type = 2
		self.height = 35
		self.i = 0
		self.j = 0
		self.k = 0
		self.queenmovementlist = []
		self.image = enemy_queen_IMG

class enemy_pawn:
	def __init__(self):
		self.istaken = 0
		self.type = 1
		self.height = 21
		self.i = 0
		self.j = 0
		self.k = 0
		self.image = enemy_pawn_IMG
		self.pawnmovementlist = []

class tank:
	def __init__(self):
		self.istaken = 0
		self.type = 3
		self.height = 35
		self.i = 0
		self.j = 0
		self.k = 0
		self.image = Tank_IMG_BASIC
		self.tankmovementlist = []