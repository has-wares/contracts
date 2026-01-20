class LoopAnim:
    def __init__(self, frames, fps=8):
        self.frames = frames
        self.i = 0
        self.acc_ms = 0
        self.frame_ms = int(1200 / fps)

    def update(self, dt_ms, df):
        self.acc_ms += dt_ms
        while self.acc_ms >= self.frame_ms:
            self.acc_ms -= self.frame_ms
            self.i = (self.i + 1) % df

    def draw(self, surface, pos):
        # pos = (x,y) top-left
        surface.blit(self.frames[self.i], pos)

    def draw_centered(self, surface, center_pos):
        img = self.frames[self.i]
        rect = img.get_rect(center=center_pos)
        surface.blit(img, rect)
