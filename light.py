import time
from Maix import GPIO
from fpioa_manager import fm

fm.register(0, fm.fpioa.GPIO0, force=True)
fm.register(17, fm.fpioa.GPIO1, force=True)
fm.register(6, fm.fpioa.GPIO2, force=True)
fm.register(7, fm.fpioa.GPIO3, force=True)
fm.register(8, fm.fpioa.GPIO4, force=True)
fm.register(1, fm.fpioa.GPIOHS2, force=True)
fm.register(2, fm.fpioa.GPIOHS3, force=True)
fm.register(3, fm.fpioa.GPIOHS4, force=True)
fm.register(16, fm.fpioa.GPIOHS5, force=True)

led1 = GPIO(GPIO.GPIO0, GPIO.OUT)
led2 = GPIO(GPIO.GPIO1, GPIO.OUT)
led_r = GPIO(GPIO.GPIO2, GPIO.OUT)
led_g = GPIO(GPIO.GPIO3, GPIO.OUT)
led_b = GPIO(GPIO.GPIO4, GPIO.OUT)
key1 = GPIO(GPIO.GPIOHS2, GPIO.IN, GPIO.PULL_NONE)
key2 = GPIO(GPIO.GPIOHS3, GPIO.IN, GPIO.PULL_NONE)
key3 = GPIO(GPIO.GPIOHS4, GPIO.IN, GPIO.PULL_NONE)
key = GPIO(GPIO.GPIOHS5, GPIO.IN, GPIO.PULL_DOWN)

def get_key():
    if key1.value() == False:
        while key1.value() == False: pass
        return 1
    if key2.value() == False:
        while key2.value() == False: pass
        return 2
    if key3.value() == False:
        while key3.value() == False: pass
        return 3
    if key.value() == False:
        while key.value() == False: pass
        return 4
    return 0

def show_color(color = 0):
    '''
    color = 0 - black
    color = 1 - red
    color = 2 - yellow
    color = 3 - green
    color = 4 - cyan
    color = 5 - blue
    color = 6 - magenta
    color = 7 - white
    '''
    color %= 8
    led_r.value(color not in (1, 2, 6, 7))
    led_g.value(color not in (2, 3, 4, 7))
    led_b.value(color not in (4, 5, 6, 7))

status = False
color = 0
while True:
    led1.value(status)
    led2.value(not status)
    show_color(color)
    time.sleep_ms(300)
    #print("LED (%d,%d)" % (led1.value(), led2.value()))
    key_num = get_key()
    print(key_num)
    if key_num == 2:
        status = not status
    if key_num == 1:
        color = (color + 8 - 1) % 8
    if key_num == 3:
        color = (color + 8 + 1) % 8
    if key_num == 4:
        led1.value(True)
        led2.value(True)
        show_color(0)
        break

#fm.unregister(0)
#fm.unregister(17)
