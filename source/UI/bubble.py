import pygame

class Bubble:
  def __init__(self, text, font, role="ai", max_width=360):
    self.text = text
    self.font = font
    self.role = role
    self.max_width = max_width
    self.ai_color = (55, 65, 81)
    self.user_color = (59, 130, 246)
    self.text_color = (240, 240, 240)
    self.padding_x = 16
    self.padding_y = 10
    self.lines = self.wrap_text(text)
    self.text_surfs = [self.font.render(line, True, self.text_color) for line in self.lines]
    self.width = max(s.get_width() for s in self.text_surfs) + self.padding_x * 2
    self.height = len(self.text_surfs) * self.font.get_linesize() + self.padding_y * 2

  def wrap_text(self, text):
    words = text.split(" ")
    lines = []
    current_line = ""
    for word in words:
        test = current_line + word + " "
        if self.font.size(test)[0] <= self.max_width:
          current_line = test
        else:
          lines.append(current_line)
          current_line = word + " "
    lines.append(current_line)
    return lines

  def draw(self, screen, y=20, sidebar_width=0):
    if self.role == "user":
      x = 800 - self.width - 30
      color = self.user_color
    else:
      x = 30 + sidebar_width
      color = self.ai_color

    rect = pygame.Rect(x, y, self.width, self.height)
    pygame.draw.rect(screen, color, rect, border_radius=14)

    for i, surf in enumerate(self.text_surfs):
            screen.blit(surf,(rect.x + self.padding_x, rect.y + self.padding_y + i * self.font.get_linesize()))
    return self.height + 10  # spacing between bubbles
