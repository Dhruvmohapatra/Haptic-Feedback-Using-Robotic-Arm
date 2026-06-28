import bluetooth
import RPi.GPIO as GPIO
import time

# CONFIG
ESP32_NAME = "ESP32_Flex"
RING_THRESHOLD = 3000
VIBRATION_GPIO = 18

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(VIBRATION_GPIO, GPIO.OUT)
GPIO.output(VIBRATION_GPIO, GPIO.LOW)

# ---------- BLUETOOTH ----------
print("Searching for ESP32...")

devices = bluetooth.discover_devices(
    duration=8,
    lookup_names=True
)

esp32_addr = None

for addr, name in devices:
    if name == ESP32_NAME:
        esp32_addr = addr
        break

if esp32_addr is None:
    print("ESP32 not found")
    GPIO.cleanup()
    exit(1)

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((esp32_addr, 1))

print("Connected to ESP32")

# ---------- MAIN LOOP ----------
try:

    while True:

        data = sock.recv(1024).decode().strip()

        if not data:
            continue

        values = data.split(",")

        if len(values) != 3:
            continue

        ring = int(values[2])

        print("Ring:", ring)

        if ring <= RING_THRESHOLD:

            GPIO.output(VIBRATION_GPIO, GPIO.HIGH)
            print("VIBRATION ON")

        else:

            GPIO.output(VIBRATION_GPIO, GPIO.LOW)
            print("VIBRATION OFF")

except KeyboardInterrupt:

    print("\nStopping...")

finally:

    GPIO.output(VIBRATION_GPIO, GPIO.LOW)
    GPIO.cleanup()
    sock.close()