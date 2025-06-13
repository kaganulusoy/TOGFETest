import time
import board
import busio
import digitalio
import adafruit_max31856

# SPI arayüzü başlat
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# Chip Select pini ayarla
cs = digitalio.DigitalInOut(board.D8)  # CE0 → GPIO8
cs.direction = digitalio.Direction.OUTPUT

# Sensör nesnesi oluştur
sensor = adafruit_max31856.MAX31856(spi, cs)

# Sürekli okuma döngüsü
while True:
    try:
        sicaklik = sensor.temperature
        print(f"Sıcaklık: {sicaklik:.2f} °C")
    except Exception as e:
        print("Hata:", e)
    time.sleep(1)
