import pyxel

WINDOW_H = 120
WINDOW_W = 160
CAT_H = 16
CAT_W = 16


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class cat:
    def __init__(self, img_id):
        self.pos = Vec2(0, 0)
        self.vec = 0
        self.img_cat = img_id

    def update(self, x, y, dx):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx


class Ball:
    def __init__(self):
        self.pos = Vec2(0, 0)
        self.vec = 0
        self.size = 2
        self.speed = 3
        self.color = 10  # 0~15

    def update(self, x, y, dx, size, color):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx
        self.size = size
        self.color = color


class Ball:
    def __init__(self):
        self.pos = Vec2(0, 0)
        self.vec = 0
        self.size = 2
        self.speed = 3
        self.color = 10  # 0~15

    def update(self, x, y, dx, size, color):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx
        self.size = size
        self.color = color


class App:
    def __init__(self):
        self.IMG_ID0 = 0
        self.IMG_ID1 = 1
        # self.IMG_ID2 = 2
        self.IMG_ID0_X = 60
        self.IMG_ID0_Y = 65

        pyxel.init(WINDOW_W, WINDOW_H, caption="Hello Pyxel")
        pyxel.image(self.IMG_ID0).load(0, 0, "pic/pyxel_logo_38x16.png")
        pyxel.image(self.IMG_ID1).load(0, 0, "pic/cat_16x16.png")

        # pyxel.mouse(True)
        self.mcat = cat(self.IMG_ID1)
        self.Balls = []

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        dx = pyxel.mouse_x - self.mcat.pos.x  # x軸方向の移動量(マウス座標 - cat座標)
        dy = pyxel.mouse_y - self.mcat.pos.y  # y軸方向の移動量(マウス座標 - cat座標)
        if dx != 0:
            self.mcat.update(pyxel.mouse_x, pyxel.mouse_y, dx)  # cat座標をマウス座標に更新
        elif dy != 0:
            self.mcat.update(pyxel.mouse_x, pyxel.mouse_y, self.mcat.vec)
        # else:
        #    self.mcat.update(self.mcat.pos.x, self.mcat.pos.y, self.mcat.vec)  # 静止状態

        # ====== ctrl Ball ======
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            new_ball = Ball()
            if self.mcat.vec > 0:
                new_ball.update(self.mcat.pos.x + CAT_W/2 + 6,
                                self.mcat.pos.y + CAT_H/2,
                                self.mcat.vec, new_ball.size, new_ball.color)
            else:
                new_ball.update(self.mcat.pos.x + CAT_W/2 - 6,
                                self.mcat.pos.y + CAT_H/2,
                                self.mcat.vec, new_ball.size, new_ball.color)
            self.Balls.append(new_ball)

        # ctrl ball
        ball_count = len(self.Balls)
        for i in range(ball_count):
                if 0 < self.Balls[i].pos.x and self.Balls[i].pos.x < WINDOW_W:
                    # Ball update
                    if self.Balls[i].vec > 0:
                        self.Balls[i].update(self.Balls[i].pos.x + self.Balls[i].speed,
                                             self.Balls[i].pos.y,
                                             self.Balls[i].vec, self.Balls[i].size, self.Balls[i].color)
                    else:
                        self.Balls[i].update(self.Balls[i].pos.x - self.Balls[i].speed,
                                             self.Balls[i].pos.y,
                                             self.Balls[i].vec, self.Balls[i].size, self.Balls[i].color)
                else:
                    del self.Balls[i]
                    break

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)

        pyxel.blt(self.IMG_ID0_X, self.IMG_ID0_Y, self.IMG_ID0, 0, 0, 38, 16)

        # catのベクトル
        if self.mcat.vec > 0:
            pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.IMG_ID1, 0, 0, -CAT_W, CAT_H, 5)
        else:
            pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.IMG_ID1, 0, 0, CAT_W, CAT_H, 5)

            # ====== draw Balls ======
        for ball in self.Balls:
            pyxel.circ(ball.pos.x, ball.pos.y, ball.size, ball.color)


App()
