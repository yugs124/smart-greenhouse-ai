#define BLYNK_TEMPLATE_ID "TMPL3klLl-EEt"
#define BLYNK_TEMPLATE_NAME "Smart Greenhouse"
#define BLYNK_AUTH_TOKEN "UhszGK02MjimyYhw4POtiVNXHxl_RgAj"

#include <WiFi.h>
#include <BlynkSimpleEsp32.h>
#include <DHT.h>
#include <ESP32Servo.h>

// WiFi
char ssid[] = "Jio 5g";
char pass[] = "12345678";

// Pins
#define DHTPIN 13
#define DHTTYPE DHT11
#define IR_PIN 27
#define MQ_PIN 34
#define SERVO_PIN 25

DHT dht(DHTPIN, DHTTYPE);
Servo myServo;

// Thresholds
int gasThreshold = 150;
float tempThreshold = 30.0;

void setup() {
  Serial.begin(115200);

  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);

  dht.begin();
  pinMode(IR_PIN, INPUT);

  myServo.setPeriodHertz(50);
  myServo.attach(SERVO_PIN, 500, 2400);
  myServo.write(0);

  Serial.println("Blynk Connected System Started");
}

void loop() {
  Blynk.run();

  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  int gasValue = analogRead(MQ_PIN);
  int irState = digitalRead(IR_PIN);

  if (isnan(temp) || isnan(hum)) return;

  // Send to Blynk
  Blynk.virtualWrite(V0, temp);
  Blynk.virtualWrite(V1, hum);
  Blynk.virtualWrite(V2, gasValue);
  Blynk.virtualWrite(V3, irState);

  int servoAngle = 0;

  if (temp > tempThreshold || gasValue > gasThreshold) {
    servoAngle = 90;
  }

  myServo.write(servoAngle);

  // Vent status
  Blynk.virtualWrite(V4, servoAngle > 0 ? 1 : 0);

  delay(2000);
}