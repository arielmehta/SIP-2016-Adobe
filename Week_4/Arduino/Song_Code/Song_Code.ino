int piezo_pin = 9;
int note_a4 = 440;
int whole_note = 1600;

void setup() {
  // put your setup code here, to run once:
  pinMode(piezo_pin, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  tone(piezo_pin, note_a4, whole_note);
  delayMicroseconds(1000);

}
