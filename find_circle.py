# 仅支持圆形，矩形识别不了了

import sensor
import image
import lcd
import time
import init

def get_color(r: int, g: int, b: int):
    m = max(r, g, b)
    return 'G' if m == g else 'B' if m == b else 'R'

th = 3800
while True:
    img = sensor.snapshot()
    circles = img.find_circles(threshold = th)
    for circ in circles:
        x, y, r = circ[0:3]
        color = get_color(*img.get_pixel(x, y))
        img.draw_circle(x, y, r, lcd.WHITE)
        img.draw_string(x, y, "%s\n%d" % (color, r), lcd.WHITE)
        #print("circle: x=%d, y=%d, r=%d" % circ[0:3])
    lcd.display(img)
