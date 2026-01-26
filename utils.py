import pygame


def load_frames_auto(path: str, scale_to=None):
    sheet = pygame.image.load(path).convert_alpha()

    frame_h = sheet.get_height()
    frame_w = frame_h
    num_frames = sheet.get_width() // frame_w

    frames = []
    for i in range(num_frames):
        rect = pygame.Rect(i * frame_w, 0, frame_w, frame_h)
        frame = sheet.subsurface(rect).copy()

        if scale_to is not None:
            frame = pygame.transform.smoothscale(frame, scale_to)

        frames.append(frame)

    return frames


def format_resources(camp):
    resources = camp.get('resources', {})
    resource_array = [k for k in resources]
    lines = []
    for i in resource_array:
        lines.append(f"{i.capitalize().ljust(8)} : {str(resources[i]).rjust(1)}")

    return "\n".join(lines)



def clamp(x, low, high):
    return max(low, min(x, high))



def ensure_history(game):
    game.setdefault('cmd_history', [])
    game.setdefault('history_index', 0)
    game.setdefault('history_draft', '')
    game.setdefault('h_browsing', False)

def history_push(game, cmd):
    cmd = cmd.strip()
    if not cmd:
        return

    history = game['cmd_history']
    if history and history[-1] == cmd:
        return

    history.append(cmd)
    game['history_index'] = len(history)
    game['h_browsing'] = False
    game['history_draft'] = ''

def history_up(game, cmd_text):
    history = game['cmd_history']
    if not history:
        return cmd_text

    if not game['h_browsing']:
        game['history_draft'] = cmd_text
        game['h_browsing'] = True

    game['history_index'] = max(0, game['history_index'] - 1)
    return history[game['history_index']]

def history_down(game):
    history = game['cmd_history']
    if not history:
        return ''

    game['history_index'] = min(len(history), game['history_index'] + 1)

    if game['history_index'] == len(history):
        game['h_browsing'] = False
        return game.get('history_draft', '')
    return history[game['history_index']]
