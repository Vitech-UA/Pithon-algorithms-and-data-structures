from PIL import Image, ImageDraw
import time
import threading
import queue

width = 320
height = 240

point_q = queue.Queue()

def draw_figure(R, G, B, ):

    img = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(img)

    n = 255
    max = 10
    step = 0

    for ix in range(width):
        for iy in range(height):
            x = 0.0
            y = 0.0
            cx = 0.008 * (ix - 3 * width / 4)
            cy = 0.008 * (iy - height / 2)
            for i in range(n):
                x1 = x * x - y * y + cx
                y1 = 2 * x * y + cy
                if (x1 > max) or (y1 > max):
                    break
                x = x1
                y = y1
                step += 1
            else:

                draw.point((ix, iy), (255, 0, 0))

    img.show()


thread_red = threading.Thread(target=draw_figure, args=(255, 0, 0))
thread_red.start()

thread_green = threading.Thread(target=draw_figure, args=(0, 255, 0))
thread_green.start()

thread_blue = threading.Thread(target=draw_figure, args=(0, 0, 255))
thread_blue.start()
