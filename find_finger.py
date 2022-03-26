import sensor, image, lcd, time
import KPU as kpu
import gc, sys

sensor_window=(224, 224)
lcd_rotation=0
sensor_hmirror=False
sensor_vflip=False
model_addr="/sd/m.kmodel"
labels = ["paper", "rock", "scissors"]

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing(sensor_window)
sensor.set_hmirror(sensor_hmirror)
sensor.set_vflip(sensor_vflip)
sensor.run(1)

lcd.init(type=1)
lcd.rotation(lcd_rotation)
lcd.clear(lcd.WHITE)

task = kpu.load(model_addr)

while(True):
    img = sensor.snapshot()
    fmap = kpu.forward(task, img)
    plist=fmap[:]
    pmax=max(plist)
    if pmax>0.6:          #识别率低于0.6的将不会显示
        max_index=plist.index(pmax)
        img.draw_string(0,0, "%.2f : %s" %(pmax, labels[max_index].strip()), scale=2)
    lcd.display(img)
