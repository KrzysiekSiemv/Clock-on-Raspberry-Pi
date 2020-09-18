#!/bin/bash
# Stworzone przez Krzysztof 'KrzysiekSiemv' Smaga
# GitHub: https://github.com/KrzysiekSiemv
import time
import math
import datetime
import locale
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
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fonts', 'font.ttf'))
    fontTime = ImageFont.truetype(font_path, 48)
    now = datetime.datetime.now()
    today_time = now.strftime("%H:%M")

    with canvas(device) as draw:
        now = datetime.datetime.now()      
        draw.text((0, 6), today_time, fill="yellow", font=fontTime) 
    time.sleep(0.1)

def weather():
    api_address = '{API_LINK}'
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fonts', 'font.ttf'))
    font = ImageFont.truetype(font_path, 16)
    fontTemp = ImageFont.truetype(font_path, 36)
    json_data = requests.get(api_address).json()
    
    ## Główny opis
    main = json_data['weather'][0]['main']
    temperature = json_data['main']['temp']

    ## Ikona
    icon_name = (json_data['weather'][0]['icon']) + ".png"
    icon_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'icons', icon_name))
    icon = Image.open(icon_path)
    icon = icon.resize((52, 52), Image.ANTIALIAS)

    
    with canvas(device) as draw:
        draw.text((0, 0), "Pogoda", fill="white", font=font)
        draw.text((0, 12), main, fill="white", font=font)
        draw.text((0, 24), str(temperature).split(".")[0] + "°C", fill="white", font=fontTemp)
        draw.bitmap((80, 16), icon, fill="white")
    
    time.sleep(0.1)
    
def date():
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fonts', 'font.ttf'))
    fontDay = ImageFont.truetype(font_path, 48)  
    fontWeek = ImageFont.truetype(font_path, 14)  
    fontMonth = ImageFont.truetype(font_path, 18)   
    locale.setlocale(locale.LC_TIME, "pl_PL") 
    now = datetime.datetime.now()  
    today_day = now.strftime("%d")
    today_month = now.strftime("%B")
    today_week = now.strftime("%A")
    with canvas(device) as draw:
        now = datetime.datetime.now()
        draw.text((0, 0), today_day, fill="yellow", font=fontDay)
        draw.text((6, 40), today_month, fill="yellow", font=fontMonth)
        draw.text((52, 16), today_week, fill="yellow", font=fontWeek)
        
def yes():
    clock()
    time.sleep(10)
    date()
    time.sleep(5)
    weather()
    time.sleep(5)

def main():
    while True:
        device.contrast(4)
        yes()
        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

