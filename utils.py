import pygame

def load_frames_auto(path: str, scale_to=None):
    """
    Loads a single-row sprite sheet where frames are square and frame size == sheet height.
    Your case: 15360x640 => frame_w=640 frame_h=640 => 24 frames

    scale_to: (w,h) to resize each frame (optional)
    drop_last_blank: if last frame is empty / junk, remove it
    """
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
