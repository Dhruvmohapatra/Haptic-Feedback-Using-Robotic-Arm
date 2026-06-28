#include "BluetoothSerial.h"

// ===== Vibration Motor =====
#define VIBRATION_PIN 5   // D5 (GPIO 5)

// ===== Flex Sensor Pins =====
#define FLEX1 34   // Index finger
#define FLEX2 35   // Middle finger
#define FLEX3 32   // Ring finger

BluetoothSerial SerialBT;

// ===== Vibration control variables =====
bool vibrateRequest = false;
unsigned long vibrateStartTime = 0;
const unsigned long VIBRATE_DURATION = 2000; // 2 seconds

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_Flex");   // Bluetooth name

  pinMode(VIBRATION_PIN, OUTPUT);
  digitalWrite(VIBRATION_PIN, LOW);

  delay(1000);
  Serial.println("ESP32 started: Sending flex data & listening for vibration command");
}

void loop() {
  /* ===== 1. Read Flex Sensors ===== */
  int flex1 = analogRead(FLEX1);
  int flex2 = analogRead(FLEX2);
  int flex3 = analogRead(FLEX3);

  String data = String(flex1) + "," + String(flex2) + "," + String(flex3);

  // Send data continuously to Raspberry Pi
  SerialBT.println(data);
  Serial.println("Sent: " + data);

  /* ===== 2. Receive Command from Raspberry Pi ===== */
  if (SerialBT.available()) {
    String command = SerialBT.readStringUntil('\n');
    command.trim();

    Serial.println("Received: " + command);

    if (command == "VIBRATE_ON") {
      vibrateRequest = true;
      vibrateStartTime = millis();
      digitalWrite(VIBRATION_PIN, HIGH);
      Serial.println("Vibration ON");
    }

    if (command == "VIBRATE_OFF") {
      vibrateRequest = false;
      digitalWrite(VIBRATION_PIN, LOW);
      Serial.println("Vibration OFF");
    }
  }

  /* ===== 3. Auto stop vibration after 2 sec ===== */
  if (vibrateRequest && (millis() - vibrateStartTime >= VIBRATE_DURATION)) {
    digitalWrite(VIBRATION_PIN, LOW);
    vibrateRequest = false;
    Serial.println("Vibration auto-stopped after 2 sec");
  }

  delay(200); // Data refresh rate
}