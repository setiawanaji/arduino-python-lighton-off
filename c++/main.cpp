int data;
int LED = 13;

void setup()
{
  Serial.begin(9600);     // initialize serial COM at 9600 boudrate
  pinMode(LED, OUTPUT);   // declare pin 13 as output
  digitalWrite(LED, LOW); // turn off the light as beginning
}
void loop()
{
  while (Serial.available())
  {
    data = Serial.read();
  }

  if (data == '1')
  {
    digitalWrite(LED, HIGH); // turn on the light
  }
  else if (data == '0')
  {
    digitalWrite(LED, LOW); // turn off the light
  }
}