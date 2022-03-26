import network, time
from machine import UART
from Maix import GPIO
from fpioa_manager import fm
from network_espat import wifi
import lcd

encode = "utf-8"

def wifi_init():
    wifi.init()
    time.sleep(1)
    at_init_code = [
        'AT+CWMODE=2',
        'AT+CWSAP="ESP8266","12345678",11,3',
        'AT+CIPAP="192.168.4.1"',
        #'AT+RST',  # 这句貌似会影响使用
        'AT+CIPMUX=1',
        'AT+CIPSERVER=1,8080',
    ]
    for code in at_init_code:
        ok = wifi.at_cmd(code + "\r\n")
        print(ok)
        time.sleep_ms(1000)

def send(str):
    wifi.at_cmd("AT+CIPSEND=0,%d\r\n" % len(str.encode(encode)))
    wifi.at_cmd(str)
    time.sleep_ms(10)

def read_receive():
    temp = wifi.uart.read()
    if temp != None:
        try:
            #encode = "utf-8"
            temp = temp.decode(encode)
        except:  # 如果客户端使用其它（如 GBK）编码发送信息会报错
            #encode = "gbk"
            #temp = temp.decode(encode)
            warning = "Warning: Please using UTF-8 encode, don't use other encode."
            print(warning)
            send(warning)
            return None
        #print(temp)
        ipd = temp.find("+IPD")  # 居然不支持海象运算符
        if ipd != -1:
            pos = temp.find(":", ipd) + 1
            #print(str(ipd)+','+str(pos))
            return temp[pos:]
    return None

if __name__ == "__main__":
    wifi_init()
    while True:
        msg = read_receive()
        if msg != None:
            lcd.clear(lcd.BLACK)
            lcd.draw_string(10, 10, msg, lcd.RED, lcd.BLACK)
            send("Hello, %s\r\n" % msg)
