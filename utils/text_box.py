import pygame
from .settings import *

color_active = '#ffffff'
color_inactive = '#8d8d8d'

class text_box:

    def __init__(self, x, y, w, h, text='000000'):
        self.rect = pygame.Rect(x, y, w, h)
        self.rect.midbottom = (100, res_y - 12)
        self.color = color_inactive
        self.text = text
        self.text_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event, allowedInput):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and not self.active:
                self.active = True
                self.color = color_active

            else:
                self.active = False
                self.color = color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

                elif len(self.text) < 6:
                    for i in allowedInput:
                        if i == event.unicode.upper():
                            self.text += event.unicode
                            self.text = self.text.upper()
                            
    def draw(self, screen):
        self.text_surface = font.render(self.text, True, self.color)
        screen.blit(self.text_surface, (((self.rect.width / 2) - self.text_surface.get_width() / 2 + 18), self.rect.y + 12))
        pygame.draw.rect(screen, self.color, self.rect, 6)