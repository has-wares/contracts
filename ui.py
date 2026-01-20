import pygame
import uiconfig

TEXT_ENTRY = pygame.Rect(
    uiconfig.ENTRY_BOX_X,
    uiconfig.ENTRY_BOX_Y,
    uiconfig.ENTRY_BOX_WIDTH,
    uiconfig.ENTRY_BOX_HEIGHT
    )

RESPONSE_BOX = pygame.Rect(
    uiconfig.RESPONSE_BOX_X,
    uiconfig.RESPONSE_BOX_Y,
    uiconfig.RESPONSE_BOX_WIDTH,
    uiconfig.RESPONSE_BOX_HEIGHT
    )

BONFIRE_BOX = pygame.Rect(
    uiconfig.BONFIRE_BOX_X,
    uiconfig.BONFIRE_BOX_Y,
    uiconfig.BONFIRE_BOX_WIDTH,
    uiconfig.BONFIRE_BOX_HEIGHT
    )

ALCHEMY_BOX = pygame.Rect(
    uiconfig.ALCHEMY_BOX_X,
    uiconfig.ALCHEMY_BOX_Y,
    uiconfig.ALCHEMY_BOX_WIDTH,
    uiconfig.ALCHEMY_BOX_HEIGHT
)

COOKING_BOX = pygame.Rect(
    uiconfig.COOKING_BOX_X,
    uiconfig.COOKING_BOX_Y,
    uiconfig.COOKING_BOX_WIDTH,
    uiconfig.COOKING_BOX_HEIGHT
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


def draw_scrollable_text(surface, lines, scroll_lines, font, color, rect, line_spacing=4):
    old_clip = surface.get_clip()
    surface.set_clip(rect)

    x = rect.x + 6
    y = rect.y + 6

    line_h = font.get_height() + line_spacing
    max_visible = max(1, (rect.h - 12) // line_h)

    total = len(lines)
    max_scroll = max(0, total - max_visible)   # <-- key line

    if scroll_lines < 0:
        scroll_lines = 0
    if scroll_lines > max_scroll:
        scroll_lines = max_scroll

    end = total - scroll_lines
    start = max(0, end - max_visible)

    for line in lines[start:end]:
        img = font.render(str(line), True, color)
        surface.blit(img, (x, y))
        y += line_h

    surface.set_clip(old_clip)

    return scroll_lines, max_scroll

