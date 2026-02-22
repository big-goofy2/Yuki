class DropDown:
    def __init__(self, x, y, w, h, options):
        self.rect = pygame.Rect(x, y, w, h)
        self.options = options
        self.expanded = False
        self.selected_option = "Select Language"
        self.option_rects = []
        for i in range(len(options)):
            rect = pygame.Rect(x, y + (i + 1) * h, w, h)
            self.option_rects.append(rect)

    def draw(self, surf):
        pygame.draw.rect(surf, (100, 100, 100), self.rect, border_radius=5)
        text_surf = font.render(self.selected_option, True, (255, 255, 255))
        surf.blit(text_surf, (self.rect.x + 10, self.rect.y + (self.rect.h//4)))

        if self.expanded:
            for i, opt_rect in enumerate(self.option_rects):
                color = (80, 80, 80)
                if opt_rect.collidepoint(pygame.mouse.get_pos()):
                    color = (120, 120, 120)
                
                pygame.draw.rect(surf, color, opt_rect)
                pygame.draw.rect(surf, (255, 255, 255), opt_rect, 1) # Border
                opt_text = font.render(self.options[i], True, (255, 255, 255))
                surf.blit(opt_text, (opt_rect.x + 10, opt_rect.y + (opt_rect.h//4)))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.expanded = not self.expanded
            
            if self.expanded:
                for i, opt_rect in enumerate(self.option_rects):
                    if opt_rect.collidepoint(event.pos):
                        self.selected_option = self.options[i]
                        self.expanded = False
                        print(f"Switched to: {self.selected_option}")
