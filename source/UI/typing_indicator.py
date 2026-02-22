class TypingBubble:
    def __init__(self, name, x, y,FONT):
        self.x = x
        self.y = y
        self.text_surf = FONT.render(f"{name} is typing", True, (80, 80, 80))
        self.text_surf.set_alpha(180)
        self.dot_offsets = [0.0, -3.0, -6.0] 
        self.speeds = [-0.4, -0.4, -0.4]
        self.max_up, self.max_down = -8.0, 0.0
        self.padding = 15
        self.dot_radius = 3
        self.dot_gap = 6
        
    def draw(self, surface):
        dots_area_width = (self.dot_radius * 6) + (self.dot_gap * 2)
        bubble_width = self.text_surf.get_width() + dots_area_width + (self.padding * 2) + 10
        bubble_height = 35
        text_x = self.x + self.padding
        text_y = self.y + (bubble_height // 2 - self.text_surf.get_height() // 2)
        surface.blit(self.text_surf, (text_x, text_y))
        dots_start_x = text_x + self.text_surf.get_width() + 12
        
        for i in range(3):
            self.dot_offsets[i] += self.speeds[i]
          
            if self.dot_offsets[i] <= self.max_up:
                self.dot_offsets[i] = self.max_up
                self.speeds[i] *= -1
            elif self.dot_offsets[i] >= self.max_down:
                self.dot_offsets[i] = self.max_down
                self.speeds[i] *= -1
            
            d_x = dots_start_x + (i * (self.dot_radius * 2 + self.dot_gap))
            d_y = self.y + 22 + self.dot_offsets[i]
            pygame.draw.circle(surface, (150, 150, 155), (int(d_x), int(d_y)), self.dot_radius)
