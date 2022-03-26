# 仅支持圆形和矩形

import sensor
import image
import lcd
import time
import init

sensor.set_pixformat(sensor.GRAYSCALE)
th = 3800
while True:
    img = sensor.snapshot()
    circles = img.find_circles(threshold = th)
    #rectangles = img.find_rects()
    for circ in circles:
        img.draw_circle(circ[0], circ[1], circ[2], lcd.WHITE)
        print("circle: x=%d, y=%d, r=%d" % circ[0:3])
    #for rec in rectangles:
        #img.draw_rectangle(rec[0], rec[1], rec[2], rec[3], lcd.WHITE)
        #print("rectangle: x=%d, y=%d, w=%d, h=%d" % rec[0:4])
    lcd.display(img)
