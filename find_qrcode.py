import sensor
import image
import lcd
import time
import init

clock = time.clock()
while True:
    clock.tick()
    print(str(clock.fps()) + " fps")
    img = sensor.snapshot()
    #img.replace(img, hmirror = False, vflip = True)
    res = []
    for j in range(0, 2):
        for i in range(0, 4):
            img.replace(img, hmirror = bool(i // 2), vflip = bool(i % 2))
            res += img.find_qrcodes()
        img.invert()
    fps = clock.fps()
    if len(res) > 0:
        img.draw_string(2, 2, res[0].payload(), color=(0,128,0), scale=2)
        print(res[0].payload())
    lcd.display(img)
