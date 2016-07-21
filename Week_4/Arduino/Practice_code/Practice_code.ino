
int LEDPIN = 4;
int LEDPIN_2 = 5;
void setup() {
  // put your setup code here, to run once:
  pinMode(LEDPIN, OUTPUT);
  pinMode(LEDPIN_2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LEDPIN, HIGH);
  digitalWrite(LEDPIN_2, LOW);
  delay(563);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN_2, HIGH);
  delay(188);
  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(750);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN_2,HIGH);
  delay(750);
  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(750);
  digitalWrite(LEDPIN_2, HIGH);
  digitalWrite(LEDPIN,LOW);
  delay(1500);
  digitalWrite(LEDPIN, HIGH);
  digitalWrite(LEDPIN_2, LOW);
  delay(563);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN_2, HIGH);
  delay(188);
  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(750);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN_2,HIGH);
  delay(750);
  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(750);
  digitalWrite(LEDPIN_2, HIGH);
  digitalWrite(LEDPIN,LOW);
  delay(1500);

  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(375);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN_2,HIGH);
  delay(375);
  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(1125);
  digitalWrite(LEDPIN_2, HIGH);
  digitalWrite(LEDPIN,LOW);
  delay(375);
  digitalWrite(LEDPIN, HIGH);
  digitalWrite(LEDPIN_2, LOW);
  delay(750);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN_2, HIGH);
  delay(1500);
  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(375);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN_2,HIGH);
  delay(375);
  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(750);
  digitalWrite(LEDPIN_2, HIGH);
  digitalWrite(LEDPIN,LOW);
  delay(750);

  digitalWrite(LEDPIN, HIGH);
  digitalWrite(LEDPIN_2, LOW);
  delay(750);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN_2, HIGH);
  delay(750);
  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(750);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN_2,HIGH);
  delay(563);
  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(188);
  digitalWrite(LEDPIN_2, HIGH);
  digitalWrite(LEDPIN,LOW);
  delay(750);

  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(750);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN_2,HIGH);
  delay(750);
  digitalWrite(LEDPIN_2, LOW);
  digitalWrite(LEDPIN,HIGH);
  delay(1500);
  digitalWrite(LEDPIN,LOW);
  delay(5000);
}
