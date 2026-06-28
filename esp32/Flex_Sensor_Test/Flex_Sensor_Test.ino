// ===== Flex Sensor Pins =====
#define FLEX1 34   // Index finger
#define FLEX2 35   // Middle finger
#define FLEX3 32   // Ring finger

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("ESP32 Flex Sensor Test");
}

void loop() {
  int flex1 = analogRead(FLEX1);
  int flex2 = analogRead(FLEX2);
  int flex3 = analogRead(FLEX3);

  Serial.print("Index: ");
  Serial.print(flex1);
  Serial.print(" | Middle: ");
  Serial.print(flex2);
  Serial.print(" | Ring: ");
  Serial.println(flex3);

  delay(200);   // refresh rate
}