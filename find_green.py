import sensor
import image
import lcd
import time
import init

thresholds = [
    {"name": "R", "th": (0, 70, 42, 65, 52, 8)},
    {"name": "G", "th": (0, 80, -70, -10, -0, 30)},
    {"name": "B", "th": (0, 80, -128, 35, -128, -18)},
    {"name": "Y", "th": (0, 80, -24, 43, 66, 21)},
]
#red_threshold  =  (60, 68,  50,  62,  28,  42)  #(55, 70, 42, 65, 52, 8)
#green_threshold=  (85, 95, -80, -49,  55,  70)  #(0, 88, -42, -6, -9, 13)
#blue_threshold =  (79, 85, -24, -11, -27, -15)  #(0, 80, -128, 35, -128, -18)
#yellow_threshold =(69, 80,   5,  21,  55,  73)  #(88, 95, 0, -44, 93, 48)
#green_threshold = (0,   80,  -70,   -10,   -0,   30)
while True:
    img = sensor.snapshot()
    img.mean(2)
    for color in thresholds:
        blobs = img.find_blobs([color["th"]])
        if blobs:
            for b in blobs:
                if b[4] < 200: continue
                tmp = img.draw_rectangle(b[0:4])
                #tmp = img.draw_cross(b[5], b[6])
                img.draw_string(b[5], b[6], color["name"], lcd.WHITE)
                #c = img.get_pixel(b[5], b[6])
    lcd.display(img)
