import pygame
import utils

def handle_events(
    game,
    cmd_text,
    response_lines,
    scroll_lines,
    *,
    dispatch_command,
    MAX_LOG_LINES,
):

    utils.ensure_history(game)
    running = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEWHEEL:

            scroll_lines += event.y
            if scroll_lines < 0:
                scroll_lines = 0

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                cmd_text = utils.history_up(game, cmd_text)
            elif event.key == pygame.K_DOWN:
                cmd_text = utils.history_down(game)

            elif event.key == pygame.K_RETURN:
                cmd = cmd_text.strip()
                if not cmd:
                    cmd_text = ''
                output = dispatch_command(cmd, game)
                cmd_text = ""
                utils.history_push(game, cmd)

                if output:
                    if isinstance(output, str):
                        response_lines.append(output)
                    else:
                        response_lines.extend(output)

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

    return running, cmd_text, response_lines, scroll_lines
