import pygame
from towers import ArrowTower, ArtilleryTower, MagicTower, DefenderTower

pygame.font.init()

PANEL_RECT = pygame.Rect(740, 10, 250, 260)
BUTTONS = [
    {"label": "Arrow", "rect": pygame.Rect(755, 30, 220, 35), "color": ArrowTower().__getattribute__("colour")},
    {"label": "Artillery", "rect": pygame.Rect(755, 75, 220, 35), "color": ArtilleryTower().__getattribute__("colour")},
    {"label": "Magic", "rect": pygame.Rect(755, 120, 220, 35), "color": MagicTower().__getattribute__("colour")},
    {"label": "Defender", "rect": pygame.Rect(755, 165, 220, 35), "color": DefenderTower().__getattribute__("colour")},
]
MONEY_RECT = pygame.Rect(755, 210, 220, 20)
LIVES_RECT = pygame.Rect(755, 235, 220, 20)


def _get_font():
    try:
        return pygame.font.Font(None, 24)
    except Exception:
        return None


FONT = _get_font()


def draw_ui(screen, money, selected_tower=None, lives=None):
    pygame.draw.rect(screen, (40, 40, 60), PANEL_RECT)
    pygame.draw.rect(screen, (255, 255, 255), PANEL_RECT, 2)

    for button in BUTTONS:
        if selected_tower is not None and button["label"] == selected_tower:
            pygame.draw.rect(screen, (220, 40, 40), button["rect"])
            pygame.draw.rect(screen, (255, 255, 255), button["rect"], 3)
        else:
            pygame.draw.rect(screen, button["color"], button["rect"])
            pygame.draw.rect(screen, (255, 255, 255), button["rect"], 2)

        if FONT is not None:
            try:
                text_surface = FONT.render(button["label"], True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=button["rect"].center)
                screen.blit(text_surface, text_rect)
            except Exception:
                pass

    if FONT is not None:
        try:
            money_surface = FONT.render(f"Money: {money}", True, (255, 255, 255))
            screen.blit(money_surface, MONEY_RECT.topleft)
            if lives is not None:
                lives_surface = FONT.render(f"Lives: {lives}", True, (255, 255, 255))
                screen.blit(lives_surface, LIVES_RECT.topleft)
        except Exception:
            pass


def get_clicked_button(pos):
    for button in BUTTONS:
        if button["rect"].collidepoint(pos):
            return button["label"]
    return None


