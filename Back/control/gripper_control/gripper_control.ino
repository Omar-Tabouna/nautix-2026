/*
  gripper_control.ino  —  Arduino
  Reads JSON from serial: {"A2": 0|1, "A3": 0|1}
  Controls MOSFETs on pins A2 and A3.

  Wiring:
    A2 → MOSFET gate for gripper A
    A3 → MOSFET gate for gripper B
*/

#include <ArduinoJson.h>   // install via Library Manager: ArduinoJson by Benoit Blanchon

const int PIN_GRIPPER_A = A2;
const int PIN_GRIPPER_B = A3;
const int BAUD_RATE     = 9600;
const int BUF_SIZE      = 64;

char    inputBuf[BUF_SIZE];
uint8_t bufIdx = 0;

void setup() {
  pinMode(PIN_GRIPPER_A, OUTPUT);
  pinMode(PIN_GRIPPER_B, OUTPUT);
  digitalWrite(PIN_GRIPPER_A, LOW);
  digitalWrite(PIN_GRIPPER_B, LOW);
  Serial.begin(BAUD_RATE);
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      // null-terminate and parse
      inputBuf[bufIdx] = '\0';
      bufIdx = 0;

      StaticJsonDocument<64> doc;
      DeserializationError err = deserializeJson(doc, inputBuf);
      if (err) {
        // bad JSON — ignore
        return;
      }

      if (doc.containsKey("A2")) {
        digitalWrite(PIN_GRIPPER_A, doc["A2"] ? HIGH : LOW);
      }
      if (doc.containsKey("A3")) {
        digitalWrite(PIN_GRIPPER_B, doc["A3"] ? HIGH : LOW);
      }

    } else {
      if (bufIdx < BUF_SIZE - 1) {
        inputBuf[bufIdx++] = c;
      }
      // if buffer overflows just reset it
      else {
        bufIdx = 0;
      }
    }
  }
}
