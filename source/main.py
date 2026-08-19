import pygame
import random
from button import Button
from text_box import Text_box
from bubble import Bubble
from chat import Chat

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Numa")
clock = pygame.time.Clock()

# constants
running = True
state = "home"
greetings = [
   "How can I help with?",
   "Hello! How can I assist you today?"
]
{"unk_token": "[UNK]", "sep_token": "[SEP]", "pad_token": "[PAD]", "cls_token": "[CLS]", "mask_token": "[MASK]"}
chat_history = []
sidebar_width = 0 
sidebar_target_width = 0 
sidebar_speed = 10
chat = Chat()

# text
pygame.font.init()
big_font = pygame.font.SysFont("segoeui", 40)
font = pygame.font.SysFont("segoeui", 24)
small_font = pygame.font.SysFont("segoeui", 18)

# colors
white = (255, 255, 255)
gray = (128, 128, 128)
light_gray = (181, 181, 181)
dark_gray = (169, 169, 169)
blue = (0, 0, 255)
black = (0, 0, 0)

# UI
def chooseGreeting():
  global greetings
  greeting = random.choice(greetings)
  return f"{greeting}"
  
def wrap_text(text, font, max_width):
  words = text.split(" ")
  lines = []
  current_line = ""

  for word in words:
    test_line = current_line + word + " "
    if font.size(test_line)[0] <= max_width:
      current_line = test_line
    else:
      lines.append(current_line)
      current_line = word + " "
  lines.append(current_line)
  return lines
   
# button functionality
def sendPrompt():
  global state, txt_input, chat_history

  user_text = txt_input.text
  if not user_text:
    return
  chat.addMemory("user", user_text,"chat")
  chat_history.append(Bubble(user_text, small_font, role="user"))
  reply = "I'm Numa. I heard you."
  chat.addMemory("ai", reply, intent="reply")
  chat_history.append(Bubble(reply, small_font, role="ai"))
  print("User typed:", user_text)
  print(chat.memory)
  txt_input.text = ""
  state = "chat"
  
def back():
  global state
  if state == "chat":
    state = "home"
    
def toggle_sidebar(): 
  global sidebar_target_width 
  if sidebar_target_width == 0: 
    sidebar_target_width = 130
  else: 
    sidebar_target_width = 0 
  
# text
greeting_str = chooseGreeting() 
wrapped_lines = wrap_text(greeting_str, big_font, 500) 
rendered_greeting_surfaces = [big_font.render(line, True, white) for line in wrapped_lines]

# buttons
send_btn = Button(642, 480, 70, 70, "↑", sendPrompt)
back_btn = Button(20,160,70,70,"<--",back)
open_sidebar = Button(35, 50,50,50,">",toggle_sidebar)

# rects
bg_border = pygame.Rect(0, 0, 800, 200)
bg = pygame.Rect(0, 185, 800, 415)
logo = pygame.Rect(35, 50, 50, 50)
prompt_bar = pygame.Rect(220, 480, 400, 70)
txt_input = Text_box(220, 480, 400, 70)
sidebar = pygame.Rect(0,0,0,600)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    send_btn.handle_event(event)
    txt_input.handle_event(event)
    if state == "chat":
      back_btn.handle_event(event)
    mouse_pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if logo.collidepoint(event.pos):
        open_sidebar.handle_event(event)
        
  if sidebar_width < sidebar_target_width: 
    sidebar_width += sidebar_speed 
    if sidebar_width > sidebar_target_width: 
      sidebar_width = sidebar_target_width 
  elif sidebar_width > sidebar_target_width: 
    sidebar_width -= sidebar_speed 
    if sidebar_width < sidebar_target_width: 
      sidebar_width = sidebar_target_width 
  sidebar.width = sidebar_width
            
  screen.fill(gray)
  if state == "home":
    pygame.draw.rect(screen, dark_gray, bg)
    pygame.draw.rect(screen, gray, bg_border)
    
  pygame.draw.rect(screen, light_gray, sidebar)
  pygame.draw.rect(screen, dark_gray, logo)

  if state == "home":
    pygame.draw.rect(screen, gray, prompt_bar, border_radius=20)
    txt_input.draw(screen)
    send_btn.draw(screen)
    start_x, start_y = 215, 325
    line_h = big_font.get_linesize()
    for i, line_surf in enumerate(rendered_greeting_surfaces):
      screen.blit(line_surf, (start_x, start_y + (i * line_h)))
      
  elif state == "chat": 
    if sidebar.width == 130:
      back_btn.draw(screen)
    pygame.draw.rect(screen, gray, prompt_bar, border_radius=20) 
    txt_input.draw(screen) 
    send_btn.draw(screen) 
    y = 100
    for bubble in chat_history:
      y += bubble.draw(screen, y, sidebar_width)
    
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
