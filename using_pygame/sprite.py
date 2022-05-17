from pygame import (Surface, 
									 SRCALPHA,
									 font,
									 mouse,
									 event,
									 MOUSEBUTTONDOWN,
									 MOUSEBUTTONUP)


#===== Classes And Functions =====#
	# <Sprite Class>
class Sprite():
	def __init__(self, position, size, color, window, speed=[5, 5], prop={}):
		self.size = size
		self._window = window
		self.speed = speed
		self.color = color
		self.prop = prop
		self._object = Surface(self.size, SRCALPHA)
		self.rect = self._object.get_rect()
		
		self._object.fill(self.color)
		self.rect.x = position[0]
		self.rect.y = position[1]
	
	# <Render Method>
	def render(self): self._window.blit(self._object, self.rect)
	
	# <Position Methods>
	def set_x(self, x): self.rect.x = x
	def set_y(self, y): self.rect.y = y
	def add_x(self, x): self.rect.x += x
	def add_y(self, y): self.rect.y += y
	def get_x(self): return self.rect.x
	def get_y(self): return self.rect.y
	
	def go_center(self):
		self.rect.x = (self._window.get_width()/2)-(self.size[0]/2)
		self.rect.y = (self._window.get_height()/2)-(self.size[1]/2)
	
	# <Moving Method>
	def move(self, speed=None): # Defaulf speed is [4, 4] or self.speed
		if speed == None: self.rect = self.rect.move(self.speed)
		else: self.rect = self.rect.move(speed)
	
	# <Color Setter>
	def set_color(self, color):
		self.color = color
		self._object.fill(color)
	
	# <Sprits Event>
	def touched(self):
		for ev in event.get():
			if ev.type == MOUSEBUTTONDOWN:
				return self.rect.collidepoint(mouse.get_pos())
				break
			elif ev.type == MOUSEBUTTONUP:
				return False
				break
	
	def colliderect(self, sprite):
		return self.rect.colliderect(sprite.rect)
	
	@staticmethod
	def clone(spr):
		return Sprite(
			(spr.get_x(), spr.get_y()),
			spr.size,
			spr.color,
			spr._window,
			spr.speed,
			spr.prop
		)
####END CLASSES####

	# <Render All Sprites Function>
def render_all(sprites=[]):
	for i in sprites:
		i.render()