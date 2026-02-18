class Bubble:
  def __init__(self,text,font):
    self.text = text
    self.y = 20
    self.AI_color = (55, 65, 81)
    self.user_color = (59, 130, 246)
    self.text_color = (240, 240, 240)
    self.font = font
    self.text_surf = self.font.render(self.text, True, self.text_color) 
    self.text_rect = self.text_surf.get_rect()
    self.padding_x = 20 
    self.padding_y = 10 
    self.width = self.text_rect.width + self.padding_x 
    self.height = self.text_rect.height + self.padding_y
    
  def draw(self,screen,current_role):
    if current_role == "user": 
      x = 800 - self.width - 40 
    else: 
      x = 40
    rect = pygame.Rect(x, self.y, self.width, self.height)
    screen.blit(self.text_surf, (rect.x + 10, rect.y + 5))
