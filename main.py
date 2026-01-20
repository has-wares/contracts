import pygame
import uiconfig
import ui
import utils
from commands import dispatch_command
from animator import LoopAnim
from game import new_game

pygame.init()
screen = pygame.display.set_mode((uiconfig.WINDOW_WIDTH, uiconfig.WINDOW_HEIGHT))
pygame.display.set_caption("CONTRACTS")
pygame.key.set_repeat(300, 40)
clock = pygame.time.Clock()
font = pygame.font.Font(None, uiconfig.INPUT_FONT_SIZE)

frames = utils.load_frames_auto(
    "assets/campfire_anim.png",
    scale_to=(ui.BONFIRE_BOX.w, ui.BONFIRE_BOX.h))

fire = LoopAnim(frames, fps=8)
game = new_game()
cmd_text = ""
response_lines = []     # list[str]
scroll_lines = 0        # how many lines up from the bottom we are
MAX_LOG_LINES = 500

running = True


while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEWHEEL:
            # wheel up -> scroll up, wheel down -> scroll down
            scroll_lines += event.y
            if scroll_lines < 0:
                scroll_lines = 0

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                out = dispatch_command(cmd_text, game)
                cmd_text = ""

                if out:
                    response_lines.extend(str(out).splitlines())
                    if len(response_lines) > MAX_LOG_LINES:
                        response_lines = response_lines[-MAX_LOG_LINES:]
                    scroll_lines = 0

            elif event.key == pygame.K_BACKSPACE:
                cmd_text = cmd_text[:-1]

            elif event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_PAGEUP:
                scroll_lines += 3

            elif event.key == pygame.K_PAGEDOWN:
                scroll_lines -= 3
                if scroll_lines < 0:
                    scroll_lines = 0

            else:
                cmd_text += event.unicode

    fire.update(dt, 8)
    screen.fill(uiconfig.BLACK)
    fire.draw_centered(screen, ui.BONFIRE_BOX.center)

    ui.draw_rect(screen, uiconfig.WHITE, ui.TEXT_ENTRY)
    ui.draw_rect(screen, uiconfig.WHITE, ui.RESPONSE_BOX)
    ui.draw_rect(screen, uiconfig.RED, ui.BONFIRE_BOX)

    ui.draw_text(screen, cmd_text, font, uiconfig.WHITE, ui.TEXT_ENTRY)
    scroll_lines, max_scroll = ui.draw_scrollable_text(
        screen, response_lines, scroll_lines, font, uiconfig.WHITE, ui.RESPONSE_BOX
    )

    pygame.display.flip()

pygame.quit()
