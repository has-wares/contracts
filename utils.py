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

def get_fire_heat(game):
    return f"FIRE HEAT: {game['fire_heat']}"

def get_fire_intensity(game):
    return f"FIRE INTENSITY: {game['fire_intensity']}"

def clamp(x, low, high):
    return max(low, min(x, high))


def update_fire_intensity(camp):
    heat = clamp(camp.get("fire_heat", 0), 0, 60)
    camp["fire_heat"] = heat
    if heat < 11:
        camp["fire_intensity"] = "FEEBLE"
    elif heat < 26:
        camp["fire_intensity"] = "CALM"
    elif heat < 41:
        camp["fire_intensity"] = "CRACKLING"
    else:
        camp["fire_intensity"] = "ROARING"

