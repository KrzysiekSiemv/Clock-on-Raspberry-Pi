# Malinowy zegarek
Skrypt zegara z kalendarzem oraz pogodą wymagającą OpenWeatherMap API napisana w Python 3.7.
Ten skrypt jest napisany dla ekranu 1.3 cala OLED HAT SH1106.
Abu skrypt mógł zadziałać dla tego ekranu, postępuj zgodnie z instrukcją napisaną [tutaj](https://www.waveshare.com/w/upload/4/46/1.3inch_OLED_HAT_User_Manual_EN.pdf)<br>
<img src="https://www.waveshare.com/media/catalog/product/cache/1/image/800x800/9df78eab33525d08d6e5fb8d27136e95/1/_/1.3inch-oled-hat-3_2.jpg" width=360px />
<br>
###### (obrazek nie przedstawia screena ze skryptu. jest to zdjęcie ze strony producenta)
<br>Aby pogoda działała poprawnie dodaj swój adres API ze strony 
<br>https://openweathermap.org/api
<br>I wklej w miejsce `{API_LINK}`
<br><br>Pamiętaj aby pobrać całe repozytory, gdyż zawiera ono tutaj odpowiednią czcionkę oraz ikony do pogody. Jest także oddzielny skrypt nazwany clock.py, który zawiera sam skrypt zegara z datą. Nie wymaga połączenia z Internetem ani pobrania folderu "icons".
<br><br>Aby uruchomić skrypt wpisz w terminalu Raspberry Pi:
<br>
`sudo python3 script.py`
