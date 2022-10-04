
#include "Arduino.h"
#include "EspMQTTClient.h" /* https://github.com/plapointe6/EspMQTTClient */
                           /* https://github.com/knolleary/pubsubclient */
#define PUB_DELAY (15 * 1000) /* 15 seconds */

// Init structure with correct values
EspMQTTClient client(
  "TP-Link_6544",
  "8sk_95*U",
  "192.168.0.101",
  "esp8266",
  "strong_password"
);

void setup() {
  Serial.begin(9600);  
}

void onConnectionEstablished() {
  return;
}

long last = 0;

void pubRpiLed() {
  long now = millis();

  // Verify is timeout expired
  if (client.isConnected() && (now - last > PUB_DELAY)) {
    client.publish("led/single", "some cmd to LED");
    last = now;
  }
}

void loop() {
  client.loop();
  pubRpiLed();
}
