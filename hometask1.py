from graph import *
import math


def background():
    brushColor(85, 68, 0)
    rectangle(0, 0, 792, 400)
    brushColor(128, 102, 0)
    penColor(128, 102, 0)
    rectangle(0, 400, width, height)


def window(x1, y1, x2, y2):
    brushColor(213, 255, 230)
    penColor(213, 255, 230)
    rectangle(x1, y1, x2, y2)
    brushColor(135, 205, 222)
    penColor(135, 205, 222)
    rectangle(x1 + 10, y1 + 10, x1 + 110, y1 + 100)
    rectangle(x1 + 130, y1 + 10, x1 + 230, y1 + 100)
    rectangle(x1 + 10, y1 + 120, x1 + 110, y1 + 270)
    rectangle(x1 + 130, y1 + 120, x1 + 230, y1 + 270)


def parabola_down(x0, y0, start, finish, scale):
    k = 0.02
    while start <= finish:
        y = 0.25 * start ** 2
        point(start * 10 * scale + x0 , y * 10 * scale + y0)
        start += k


def parabola_up(x0, y0, start, finish, scale):
    k = 0.02
    while start >= finish:
        y = 0.25 * start ** 2
        point(start * 10 * scale + x0 , y * 10 * scale + y0)
        start -= k


def tangle(x, y, scale):
    brushColor(153, 153, 153)
    penColor(0, 0, 0)
    r = 50
    circle(x, y, r * scale)
    parabola_down(x - r * 0.5 * scale, y - r * 0.5 * scale, 0, 4, scale)
    parabola_down(x - r * 0.2 * scale, y - r * 0.65 * scale, -0.75, 4.5, scale)
    parabola_down(x + r * 0.1* scale, y - r * 0.8 * scale, -1, 4, scale)
    parabola_up(x - r * 0.5* scale, y - r * 0.2 * scale, 0, -2, scale)
    parabola_up(x - r * 0.1 * scale, y - r * 0.05 * scale, -0.75, -3.5, scale)
    parabola_up(x + r * 0.1 * scale, y + r * 0.2 * scale, -0.75, -3, scale)



def thread(x0, y0, scale):
    penColor(153, 153, 153)
    x = 0
    k = 0.02
    while x <= 5 * math.pi:
        y = math.cos(x)
        point(x * 20 * scale + x0, y * 20 * scale + y0)
        x += k


def ellipse(a, b, x1, y1, color):
    for x in range(-a, a):
        for y in range(-b, b):
            if 0.95 <= x ** 2 / (a ** 2) + y ** 2 / (b ** 2) <= 1:
                penColor(0, 0, 0)
                point(x + x1, y + y1)
            elif x ** 2 / (a ** 2) + y ** 2 / (b ** 2) < 1:
                if color == 1:
                    penColor(225, 128, 0)
                if color == 2:
                    penColor(131, 106, 92)
                if color == 3:
                    penColor(89, 223, 32)
                if color == 4:
                    penColor(0, 162, 232)
                if color == 5:
                    penColor(0, 0, 0)
                point(x + x1, y + y1)


def cat_right(x, y, scale, color):
    penColor(0, 0, 0)
    if color == 1:
        brushColor(225, 128, 0)
    if color == 2:
        brushColor(131, 106, 92)
    k = 100
    f = 60
    ellipse(int(70 * scale), int(30 * scale), x + k * 1.4 * scale, y, color)
    ellipse(int(100 * scale), int(60 * scale), x, y, color)
    circle(x + k * 0.65 * scale, y + f * 0.75 * scale, 40 * scale)
    ellipse(int(15 * scale), int(40 * scale), x + k * 1.1 * scale, y + f * 1.4 * scale, color)
    ellipse(int(20 * scale), int(30 * scale), x - k * 1.1 * scale, y + f * 0.5 * scale, color)
    ellipse(int(40 * scale), int(20 * scale), x - k * 0.9 * scale, y + f * 0.9 * scale, color)
    circle(x - k * 0.9 * scale, y - f * 0.5 * scale, 50 * scale)
    polygon([(x - k * 1.4 * scale, y - f * 0.75 * scale), (x - k * 1.42 * scale, y - f * 1.25 * scale),
             (x - k * 1.20 * scale, y - f * 1.15 * scale)])
    polygon([(x - k * 0.6 * scale, y - f * 1.15 * scale), (x - k * 0.38 * scale, y - f * 1.25 * scale),
             (x - k * 0.40 * scale, y - f * 0.75 * scale)])
    brushColor(255, 174, 201)
    polygon([(x - k * 1.36 * scale, y - f * 0.75 * scale), (x - k * 1.40 * scale, y - f * 1.21 * scale),
             (x - k * 1.24 * scale, y - f * 1.12 * scale)])
    polygon([(x - k * 0.56 * scale, y - f * 1.12 * scale), (x - k * 0.4 * scale, y - f * 1.21 * scale),
             (x - k * 0.44 * scale, y - f * 0.75 * scale)])
    if color == 2:
        ellipse(int(15 * scale), int(17 * scale), x - k * 1.18 * scale, y - f * 0.72 * scale, 4)
        ellipse(int(15 * scale), int(17 * scale), x - k * 0.7 * scale, y - f * 0.72 * scale, 4)
        ellipse(int(6 * scale), int(16 * scale), x - k * 1.13 * scale, y - f * 0.72 * scale, 5)
        ellipse(int(6 * scale), int(16 * scale), x - k * 0.65 * scale, y - f * 0.72 * scale, 5)
    else:
        ellipse(int(15 * scale), int(17 * scale), x - k * 1.18 * scale, y - f * 0.72 * scale, 3)
        ellipse(int(15 * scale), int(17 * scale), x - k * 0.7 * scale, y - f * 0.72 * scale, 3)
        ellipse(int(6 * scale), int(16 * scale), x - k * 1.13 * scale, y - f * 0.72 * scale, 5)
        ellipse(int(6 * scale), int(16 * scale), x - k * 0.65 * scale, y - f * 0.72 * scale, 5)
    polygon([(x - k * 0.94 * scale, y - f * 0.25 * scale), (x - k * 0.88 * scale, y - f * 0.4 * scale),
             (x - k * 1 * scale, y - f * 0.4 * scale)])
    polyline([(x - k * 1.04 * scale, y - f * 0.15 * scale), (x - k * 1 * scale, y - f * 0.15 * scale),
              (x - k * 0.94 * scale, y - f * 0.2 * scale), (x - k * 0.94 * scale, y - f * 0.25 * scale),
              (x - k * 0.94 * scale, y - f * 0.2 * scale), (x - k * 0.9 * scale, y - f * 0.15 * scale),
              (x - k * 0.84 * scale, y - f * 0.15 * scale)])


def cat_left(x, y, scale, color):
    penColor(0, 0, 0)
    if color == 1:
        brushColor(225, 128, 0)
    if color == 2:
        brushColor(131, 106, 92)
    k = 100
    f = 60
    ellipse(int(70 * scale), int(30 * scale), x - k * 1.4 * scale, y, color)
    ellipse(int(100 * scale), int(60 * scale), x, y, color)
    circle(x - k * 0.65 * scale, y + f * 0.75 * scale, 40 * scale)
    ellipse(int(15 * scale), int(40 * scale), x - k * 1.1 * scale, y + f * 1.4 * scale, color)
    ellipse(int(20 * scale), int(30 * scale), x + k * 1.1 * scale, y + f * 0.5 * scale, color)
    ellipse(int(40 * scale), int(20 * scale), x + k * 0.9 * scale, y + f * 0.9 * scale, color)
    circle(x + k * 0.9 * scale, y - f * 0.5 * scale, 50 * scale)
    polygon([(x + k * 1.4 * scale, y - f * 0.75 * scale), (x + k * 1.42 * scale, y - f * 1.25 * scale),
             (x + k * 1.20 * scale, y - f * 1.15 * scale)])
    polygon([(x + k * 0.6 * scale, y - f * 1.15 * scale), (x + k * 0.38 * scale, y - f * 1.25 * scale),
             (x + k * 0.40 * scale, y - f * 0.75 * scale)])
    brushColor(255, 174, 201)
    polygon([(x + k * 1.36 * scale, y - f * 0.75 * scale), (x + k * 1.40 * scale, y - f * 1.21 * scale),
             (x + k * 1.24 * scale, y - f * 1.12 * scale)])
    polygon([(x + k * 0.56 * scale, y - f * 1.12 * scale), (x + k * 0.4 * scale, y - f * 1.21 * scale),
             (x + k * 0.44 * scale, y - f * 0.75 * scale)])
    if color == 2:
        ellipse(int(15 * scale), int(17 * scale), x + k * 1.2 * scale, y - f * 0.72 * scale, 4)
        ellipse(int(15 * scale), int(17 * scale), x + k * 0.7 * scale, y - f * 0.72 * scale, 4)
        ellipse(int(6 * scale), int(16 * scale), x + k * 1.13 * scale, y - f * 0.72 * scale, 5)
        ellipse(int(6 * scale), int(16 * scale), x + k * 0.65 * scale, y - f * 0.72 * scale, 5)
    else:
        ellipse(int(15 * scale), int(17 * scale), x + k * 1.18 * scale, y - f * 0.72 * scale, 3)
        ellipse(int(15 * scale), int(17 * scale), x + k * 0.7 * scale, y - f * 0.72 * scale, 3)
        ellipse(int(6 * scale), int(16 * scale), x + k * 1.13 * scale, y - f * 0.72 * scale, 5)
        ellipse(int(6 * scale), int(16 * scale), x + k * 0.65 * scale, y - f * 0.72 * scale, 5)
    polygon([(x + k * 0.94 * scale, y - f * 0.25 * scale), (x + k * 0.88 * scale, y - f * 0.4 * scale),
             (x + k * 1 * scale, y - f * 0.4 * scale)])
    polyline([(x + k * 1.04 * scale, y - f * 0.15 * scale), (x + k * 1 * scale, y - f * 0.15 * scale),
              (x + k * 0.94 * scale, y - f * 0.2 * scale), (x + k * 0.94 * scale, y - f * 0.25 * scale),
              (x + k * 0.94 * scale, y - f * 0.2 * scale), (x + k * 0.9 * scale, y - f * 0.15 * scale),
              (x + k * 0.84 * scale, y - f * 0.15 * scale)])


width = 600
height = 900

windowSize(width, height)
canvasSize(width, height)

background()

window(350, 60, 590, 340)
window(80, 60, 320, 340)
window(-190, 60, 50, 340)

thread(100, 510, 0.25)
tangle(180, 500, 0.33)
thread(360, 808, 0.25)
tangle(440, 800, 0.33)
thread(100, 800, 0.5)
tangle(280, 780, 1)
thread(70, 747, 0.25)
tangle(150, 740, 0.25)
thread(550, 710, 0.25)
tangle(550, 700, 0.5)
thread(435, 640, 0.25)
tangle(400, 630, 0.75)
thread(570, 528, 0.25)
tangle(570, 530, 0.25)

cat_right(350, 500, 0.75, 1)
cat_right(400, 730, 0.33, 1)
cat_right(500, 770, 0.25, 2)
cat_left(170, 630, 0.75, 2)
cat_left(100, 500, 0.33, 1)
cat_left(550, 630, 0.25, 1)
cat_left(150, 790, 0.25, 2)

run()
