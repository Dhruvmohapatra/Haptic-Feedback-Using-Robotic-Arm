import bluetooth
from adafruit_servokit import ServoKit
import time

# Bluetooth Device Name
ESP32_NAME = "ESP32_Flex"

# Initialize PCA9685 Servo Driver
kit = ServoKit(channels=16)

# Initial Servo Positions
kit.servo[0].angle = 90
kit.servo[1].angle = 90
kit.servo[2].angle = 90
kit.servo[3].angle = 90

print("Searching for ESP32...")

devices = bluetooth.discover_devices(duration=8, lookup_names=True)

esp32_addr = None

for addr, name in devices:
    if name == ESP32_NAME:
        esp32_addr = addr
        break

if esp32_addr is None:
    print("ESP32 not found")
    exit()

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((esp32_addr, 1))

print("Connected Successfully")


def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


try:

    while True:

        data = sock.recv(1024).decode().strip()

        if not data:
            continue

        values = data.split(",")

        if len(values) != 3:
            continue

        flex1 = int(values[0])
        flex2 = int(values[1])
        flex3 = int(values[2])

        servo1 = map_value(flex1, 1800, 3500, 0, 180)
        servo2 = map_value(flex2, 1800, 3500, 0, 180)
        servo3 = map_value(flex3, 1800, 3500, 0, 180)

        servo1 = max(0, min(180, servo1))
        servo2 = max(0, min(180, servo2))
        servo3 = max(0, min(180, servo3))

        kit.servo[0].angle = servo1
        kit.servo[1].angle = servo2
        kit.servo[2].angle = servo3

        time.sleep(0.05)

except KeyboardInterrupt:

    print("Stopping Servo Controller")

finally:

    sock.close()