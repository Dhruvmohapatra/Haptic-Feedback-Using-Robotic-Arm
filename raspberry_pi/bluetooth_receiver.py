import bluetooth

# Replace with ESP32 Bluetooth name
target_name = "ESP32_Flex"

print("Searching for ESP32 device...")

nearby_devices = bluetooth.discover_devices(
    duration=8,
    lookup_names=True
)

esp32_address = "00:70:07:84:15:2E"

for addr, name in nearby_devices:
    if target_name == name:
        esp32_address = addr
        break

if esp32_address is None:
    print("Could not find ESP32_Flex device")
    exit(1)

print(f"Found ESP32 at {esp32_address}, connecting...")

# Connect to ESP32 Bluetooth SPP
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

sock.connect((esp32_address, 1))

print("Connected. Receiving data...\n")

try:
    while True:

        data = sock.recv(1024).decode("utf-8").strip()

        if data:

            # Data format:
            # flex1,flex2,flex3

            values = data.split(",")

            if len(values) == 3:

                print(
                    f"Index: {values[0]} | "
                    f"Middle: {values[1]} | "
                    f"Ring: {values[2]}"
                )

            else:

                print("Raw:", data)

except KeyboardInterrupt:

    print("\nDisconnected.")

finally:

    sock.close()