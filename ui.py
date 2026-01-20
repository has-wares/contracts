import pygame
import config

TEXT_ENTRY = pygame.Rect(
    config.ENTRY_BOX_X,
    config.ENTRY_BOX_Y,
    config.ENTRY_BOX_WIDTH,
    config.ENTRY_BOX_HEIGHT
    )

RESPONSE_BOX = pygame.Rect(
    config.RESPONSE_BOX_X,
    config.RESPONSE_BOX_Y,
    config.RESPONSE_BOX_WIDTH,
    config.RESPONSE_BOX_HEIGHT
    )

BONFIRE_BOX = pygame.Rect(
    config.BONFIRE_BOX_X,
    config.BONFIRE_BOX_Y,
    config.BONFIRE_BOX_WIDTH,
    config.BONFIRE_BOX_HEIGHT
    )

ALCHEMY_BOX = pygame.Rect(
    config.ALCHEMY_BOX_X,
    config.ALCHEMY_BOX_Y,
    config.ALCHEMY_BOX_WIDTH,
    config.ALCHEMY_BOX_HEIGHT
)

COOKING_BOX = pygame.Rect(
    config.COOKING_BOX_X,
    config.COOKING_BOX_Y,
    config.COOKING_BOX_WIDTH,
    config.COOKING_BOX_HEIGHT
)

def draw_rect(surface, color, box):
    pygame.draw.rect(surface, color, box, 2)


def draw_text(surface, text, font, color, box):
    text_font = font.render(text, True, color)
    text_rect = text_font.get_rect(midleft=(box.x + 10, box.centery))
    surface.blit(text_font, text_rect)

def draw_image(surface, image, rect):
    surface.blit(image, rect)

def draw_multiline_text(surface, text, font, color, rect, line_spacing=4):
    x = rect.x + 6
    y = rect.y + 6

    lines = str(text).splitlines()
    for line in lines:
        img = font.render(line, True, color)
        # stop if we run out of vertical space
        if y + img.get_height() > rect.bottom - 6:
            break
        surface.blit(img, (x, y))
        y += img.get_height() + line_spacing