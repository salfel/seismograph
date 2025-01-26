#include <Arduino.h>

void setup() {
  Serial.begin(9600);

  pinMode(5, INPUT);
}

void loop() {
  static bool state = false;
  static unsigned long lastMillis = 0;

  if (millis() - lastMillis > 1000) {
    state = !state;

    lastMillis = millis();
  }

  if (state) {
    Serial.println(1);
  } else {
    Serial.println(0);
  }

  delay(100);
}
