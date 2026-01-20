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
response = ""
cmd = ""
running = True


while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                response = dispatch_command(cmd_text, game)
                cmd_text = ""

            elif event.key == pygame.K_BACKSPACE:
                cmd_text = cmd_text[:-1]

            elif event.key == pygame.K_ESCAPE:
                running = False

            else:
                cmd_text += event.unicode

    fire.update(dt, 8)
    screen.fill(uiconfig.BLACK)
    fire.draw_centered(screen, ui.BONFIRE_BOX.center)

    ui.draw_rect(screen, uiconfig.WHITE, ui.TEXT_ENTRY)
    ui.draw_rect(screen, uiconfig.WHITE, ui.RESPONSE_BOX)
    ui.draw_rect(screen, uiconfig.RED, ui.BONFIRE_BOX)

    ui.draw_text(screen, cmd_text, font, uiconfig.WHITE, ui.TEXT_ENTRY)
    ui.draw_multiline_text(screen, response, font, uiconfig.WHITE, ui.RESPONSE_BOX)


    pygame.display.flip()

pygame.quit()
