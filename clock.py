#!/bin/bash
import time
import math
import datetime
import random
import requests
import os.path
import subprocess

from luma.core.render import canvas
from PIL import ImageFont
from PIL import Image

from luma.core.interface.serial import i2c, spi
from luma.core import lib

from luma.oled.device import sh1106
import RPi.GPIO as GPIO

RST_PIN        = 25
CS_PIN         = 8
DC_PIN         = 24


USER_I2C = 0
if  USER_I2C == 1:
	GPIO.setup(RST_PIN,GPIO.OUT)	
	GPIO.output(RST_PIN,GPIO.HIGH)
	
	serial = i2c(port=1, address=0x3c)
else:
	serial = spi(device=0, port=0, bus_speed_hz = 8000000, transfer_size = 4096, gpio_DC = DC_PIN, gpio_RST = RST_PIN)
device = sh1106(serial, rotate=2) #sh1106 

def clock():
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fonts', 'FreePixel.ttf'))
    fontTime = ImageFont.truetype(font_path, 38)
    fontDate = ImageFont.truetype(font_path, 20)
    now = datetime.datetime.now()
    today_time = now.strftime("%H:%M")
    today_date = now.strftime("%d/%m/%y")

    with canvas(device) as draw:
        now = datetime.datetime.now()      
        draw.text((16, 0), today_time, fill="yellow", font=fontTime)  
        draw.text((24, 40), today_date, fill="yellow", font=fontDate)
    time.sleep(0.1)

def main():
    while True:
        clock()
        device.contrast(6)
    
        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

