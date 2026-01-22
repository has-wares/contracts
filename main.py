import pygame
import uiconfig
import ui
import utils
from commands import dispatch_command
from animator import LoopAnim
from game import new_game
from input import handle_events

pygame.init()
screen = pygame.display.set_mode((uiconfig.WINDOW_WIDTH, uiconfig.WINDOW_HEIGHT))
pygame.display.set_caption("CONTRACTS")
pygame.key.set_repeat(300, 40)
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", uiconfig.INPUT_FONT_SIZE)


frames = utils.load_frames_auto(
    "assets/campfire_anim.png",
    scale_to=(ui.BONFIRE_BOX.w, ui.BONFIRE_BOX.h))

fire = LoopAnim(frames, fps=8)
game = new_game()
cmd_text = ""
response_lines = ['type help',]
scroll_lines = 0
MAX_LOG_LINES = 500

running = True


while running:
    dt = clock.tick(60)
    running, cmd_text, response_lines, scroll_lines = handle_events(game, cmd_text, response_lines,scroll_lines, dispatch_command=dispatch_command, MAX_LOG_LINES=MAX_LOG_LINES)

    fire.update(dt, 8)

    screen.fill(uiconfig.BLACK)

    fire.draw_centered(screen, ui.BONFIRE_BOX.center)

    ui.draw_rect(screen, uiconfig.WHITE, ui.TEXT_ENTRY)
    ui.draw_rect(screen, uiconfig.WHITE, ui.RESPONSE_BOX)

    # ui.draw_rect(screen, uiconfig.RED, ui.BONFIRE_BOX)
    #ui.draw_rect(screen, uiconfig.RED, ui.FIRE_INFO_BOX)

    ui.draw_rect(screen, uiconfig.WHITE, ui.RESOURCE_BOX)


    ui.draw_text(screen, cmd_text, font, uiconfig.WHITE, ui.TEXT_ENTRY)
    ui.draw_text(screen, f"FIRE HEAT: {game['fire_heat']}", font, uiconfig.WHITE, ui.FIRE_INFO_BOX)
    ui.draw_text(screen, f"FIRE: {game['fire_intensity']}", font, uiconfig.WHITE, ui.FIRE_INFO_BOX, padding=740)

    ui.draw_multiline_text(screen, utils.format_resources(game), font, uiconfig.WHITE, ui.RESOURCE_BOX)

    scroll_lines, max_scroll = ui.draw_scrollable_text(
        screen, response_lines, scroll_lines, font, uiconfig.WHITE, ui.RESPONSE_BOX
    )
    scroll_lines = max(0, min(scroll_lines, max_scroll))

    pygame.display.flip()

pygame.quit()
