import time
import board
import digitalio
import adafruit_max31856

# SPI ve Chip Select pinini ayarla
spi = board.SPI()  # GPIO11 (SCLK), GPIO10 (MOSI), GPIO9 (MISO)
cs = digitalio.DigitalInOut(board.D8)  # GPIO8 (CE0)

# Sensor
sensor = adafruit_max31856.MAX31856(spi, cs)

while True:
    try:
        sicaklik = sensor.temperature
        print(f"Sıcaklık: {sicaklik:.2f} °C")
    except Exception as e:
        print("Hata:", e)
    time.sleep(1)
