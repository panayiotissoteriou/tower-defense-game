import pygame

# approach:
# 1) build a rectangle panel on the right side of the screen
# 2) build buttons for each tower type on the panel (that take 80% of the width)
# 3) at the rightmost 20% of the width, display the money available to the player
button_rects = {
    "arrow": pygame.Rect(700, 20, 70, 30),
    "artillery": pygame.Rect(700, 60, 70, 30),
    "magic": pygame.Rect(700, 100, 70, 30),
    "defender": pygame.Rect(700, 140, 70, 30),
}

# class Button:
#     def __init__(self, x, y, width, height, color, label="", text_color=(255, 255, 255), hover_color=None):
#         self.rect = pygame.Rect(x, y, width, height)
#         self.color = color
#         self.label = label
#         self.text_color = text_color
#         self.hover_color = hover_color if hover_color is not None else color
#         self.is_hovered = False

#     def draw(self, screen):
#         color = self.hover_color if self.is_hovered else self.color
#         pygame.draw.rect(screen, color, self.rect)
#         pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

#         if self.label:
#             font = pygame.font.SysFont(None, 24)
#             text_surface = font.render(self.label, True, self.text_color)
#             text_rect = text_surface.get_rect(center=self.rect.center)
#             screen.blit(text_surface, text_rect)

#     def is_clicked(self, pos):
#         return self.rect.collidepoint(pos)




# def build_tower_buttons(panel_x=680, panel_y=10, button_width=70, button_height=30, gap=10):
#     buttons = []
#     tower_specs = [
#         ("Arrow", (218, 165, 32)),
#         ("Artillery", (178, 34, 34)),
#         ("Magic", (153, 50, 204)),
#         ("Defender", (128, 128, 128)),
#     ]

#     for index, (label, color) in enumerate(tower_specs):
#         y = panel_y + 40 + index * (button_height + gap)
#         buttons.append(Button(panel_x, y, button_width, button_height, color, label))

#     return buttons