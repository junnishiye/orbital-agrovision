#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int tempPin = A0;
int luzPin  = A1;
int vibPin  = A2;

int ledVerde = 6;
int ledAmarelo = 7;
int ledVermelho = 8;
int buzzer = 9;

void setup() {

  lcd.begin(16, 2);

  pinMode(ledVerde, OUTPUT);
  pinMode(ledAmarelo, OUTPUT);
  pinMode(ledVermelho, OUTPUT);

  pinMode(buzzer, OUTPUT);
}

void loop() {

  int leituraTemp = analogRead(tempPin);
  int luz = analogRead(luzPin);
  int vib = analogRead(vibPin);

  float tensao = leituraTemp * 5.0 / 1023.0;
  float tempC = (tensao - 0.5) * 100.0;

  bool riscoAlto = (tempC > 40 || vib > 700);
  bool atencao = (tempC > 35 || vib > 400 || luz < 300);

  digitalWrite(ledVerde, LOW);
  digitalWrite(ledAmarelo, LOW);
  digitalWrite(ledVermelho, LOW);

  noTone(buzzer);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temp:");
  lcd.print(tempC, 1);
  lcd.print("C");

  lcd.setCursor(0, 1);
  lcd.print("Luz:");
  lcd.print(luz);

  delay(2000);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Vib:");
  lcd.print(vib);

  lcd.setCursor(0, 1);

  if (riscoAlto) {

    lcd.print("RISCO ALTO");

    digitalWrite(ledVermelho, HIGH);

    tone(buzzer, 1000);

  }
  else if (atencao) {

    lcd.print("ATENCAO");

    digitalWrite(ledAmarelo, HIGH);

  }
  else {

    lcd.print("STATUS OK");

    digitalWrite(ledVerde, HIGH);

  }

  delay(2000);
}
