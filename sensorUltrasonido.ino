const int trig = 2;
const int echo = 3;
const int led = 4;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  pinMode(led,OUTPUT);
  digitalWrite(trig, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  long t;
  long d;

  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);

  t= pulseIn(echo,HIGH);
  d = t/59;
  Serial.print("distance: ");
  Serial.println(d);
  if(d>25){
    digitalWrite(led,HIGH);
  }else{
    digitalWrite(led,LOW);
  }
  delay(100);  
}
