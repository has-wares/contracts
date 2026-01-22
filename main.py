import pygame
import uiconfig
import ui
import utils
from commands import dispatch_command
from animator import LoopAnim
from game import new_game
from input import handle_events
from camping import draw_camp

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

    match game['mode']:
        case 'camp':
            camp = game['camp']
            scroll_lines = draw_camp(screen, dt, fire, camp, font, response_lines, scroll_lines)
        case 'expedition':
            pass


    ui.draw_rect(screen, uiconfig.WHITE, ui.TEXT_ENTRY)
    ui.draw_rect(screen, uiconfig.WHITE, ui.RESPONSE_BOX)
    ui.draw_text(screen, cmd_text, font, uiconfig.WHITE, ui.TEXT_ENTRY)

    pygame.display.flip()

pygame.quit()
