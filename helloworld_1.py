# Hello World Example
#
# Welcome to the MaixPy IDE!
# 1. Conenct board to computer
# 2. Select board at the top of MaixPy IDE: `tools->Select Board`
# 3. Click the connect buttion below to connect board
# 4. Click on the green run arrow button below to run the script!

import sensor, image, time, lcd, init

#lcd.init(freq=15000000)
#lcd.register(0x21, 0)
#lcd.rotation(2)
#sensor.reset()  # Reset and initialize the sensor. It will run automatically, call sensor.run(0) to stop
#sensor.set_pixformat(sensor.RGB565)  # Set pixel format to RGB565 (or GRAYSCALE)
#sensor.set_framesize(sensor.QVGA)  # Set frame size to QVGA (320x240)
#sensor.skip_frames(time = 2000)  # Wait for settings take effect.
#lcd.clear(lcd.BLACK)  # 启用后开机提示变为黑底
lcd.draw_string(100, 100, "hello MicroPython!", lcd.RED, lcd.BLACK)
time.sleep_ms(1000)
clock = time.clock()  # Create a clock object to track the FPS.

while(True):
    clock.tick()  # Update the FPS clock.
    img = sensor.snapshot()  # Take a picture and return the image.
    #img.replace(img, hmirror = False, vflip = True)
    lcd.display(img)  # Display on LCD
    #print(clock.fps())  # Note: MaixPy's Cam runs about half as fast when connected to the IDE. The FPS should increase once disconnected.

