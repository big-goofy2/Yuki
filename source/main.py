import pygame
import random
import json
from button import Button
from text_box import Text_box

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Numa")
clock = pygame.time.Clock()

# constants
running = True
active_field = None
state = "home"
greetings = [
   "How can I help with?",
   "Hello! How can I assist you today?"
]

# text
pygame.font.init()
big_font = pygame.font.Font(None, 43)
font = pygame.font.SysFont("segoeui", 24)
small_font = pygame.font.SysFont("segoeui", 18)

# colors
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = ((169, 169, 169))
blue = (0, 0, 255)
black = (0, 0, 0)

# functions
def chooseGreeting():
   global greetings
   greeting = random.choice(greetings)
   return f"{greeting}"
   
# button functionality
def sendPrompt():
  print("Prompt sent!")

# text
welcome_text = big_font.render(chooseGreeting(), True, white)

# buttons
send_btn = Button(642, 480, 70, 70, "↑", sendPrompt)

# rects
bg_border = pygame.Rect(0, 0, 800, 200)
bg = pygame.Rect(0, 185, 800, 415)
logo = pygame.Rect(35, 50, 50, 50)
prompt_bar = pygame.Rect(220, 480, 400, 70)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if state == "home":
      send_btn.handle_event(event)

  screen.fill(gray)
  if state == "home":
    pygame.draw.rect(screen, gray, bg_border, border_radius=20)
    pygame.draw.rect(screen, dark_gray, bg)
    pygame.draw.rect(screen, dark_gray, logo)
    pygame.draw.rect(screen, gray, prompt_bar, border_radius=20)
    send_btn.draw(screen)
    screen.blit(welcome_text, (250, 350))
    
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
