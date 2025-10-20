#include <Servo.h>

Servo servoMotor;

// Pin configuration
const int BUTTON_PIN = 2;
const int LED_RED = 3;
const int LED_GREEN = 12;
const int SERVO_PIN = 11;

// Seven segment display pins (common cathode)
const int SEG_A = 4;
const int SEG_B = 5;
const int SEG_C = 6;
const int SEG_D = 7;
const int SEG_E = 8;
const int SEG_F = 9;
const int SEG_G = 10;

// Program variables
int buttonState;
int lastButtonState = HIGH;
int count = 0;
const int DEBOUNCE_DELAY = 200;
bool isSystemStarted = false;

void setup() {
  // Initialize servo
  servoMotor.attach(SERVO_PIN);
  
  // Set pin modes
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  
  // Configure seven segment display pins
  pinMode(SEG_A, OUTPUT);
  pinMode(SEG_B, OUTPUT);
  pinMode(SEG_C, OUTPUT);
  pinMode(SEG_D, OUTPUT);
  pinMode(SEG_E, OUTPUT);
  pinMode(SEG_F, OUTPUT);
  pinMode(SEG_G, OUTPUT);
  
  // Initial state - all off
  clearDisplay();
  digitalWrite(LED_GREEN, LOW);
  digitalWrite(LED_RED, LOW);
  servoMotor.write(0);
}

void loop() {
  buttonState = digitalRead(BUTTON_PIN);

  // Check for button press with debounce
  if (buttonState == LOW && lastButtonState == HIGH) {
    delay(DEBOUNCE_DELAY);
    
    if (!isSystemStarted) {
      // First button press
      isSystemStarted = true;
      count = 1;
    } else {
      // Subsequent presses
      count++;
      if (count > 9) count = 1;
    }
    
    // Update outputs
    showNumber(count);
    moveServo(count);
    blinkLEDs(count);
  }
  
  lastButtonState = buttonState;
}

void showNumber(int num) {
  clearDisplay();
  
  switch (num) {
    case 1:
      digitalWrite(SEG_B, HIGH);
      digitalWrite(SEG_C, HIGH);
      break;
    case 2:
      digitalWrite(SEG_A, HIGH);
      digitalWrite(SEG_B, HIGH);
      digitalWrite(SEG_G, HIGH);
      digitalWrite(SEG_E, HIGH);
      digitalWrite(SEG_D, HIGH);
      break;
    case 3:
      digitalWrite(SEG_A, HIGH);
      digitalWrite(SEG_B, HIGH);
      digitalWrite(SEG_G, HIGH);
      digitalWrite(SEG_C, HIGH);
      digitalWrite(SEG_D, HIGH);
      break;
    case 4:
      digitalWrite(SEG_F, HIGH);
      digitalWrite(SEG_G, HIGH);
      digitalWrite(SEG_B, HIGH);
      digitalWrite(SEG_C, HIGH);
      break;
    case 5:
      digitalWrite(SEG_A, HIGH);
      digitalWrite(SEG_F, HIGH);
      digitalWrite(SEG_G, HIGH);
      digitalWrite(SEG_C, HIGH);
      digitalWrite(SEG_D, HIGH);
      break;
    case 6:
      digitalWrite(SEG_A, HIGH);
      digitalWrite(SEG_F, HIGH);
      digitalWrite(SEG_G, HIGH);
      digitalWrite(SEG_C, HIGH);
      digitalWrite(SEG_D, HIGH);
      digitalWrite(SEG_E, HIGH);
      break;
    case 7:
      digitalWrite(SEG_A, HIGH);
      digitalWrite(SEG_B, HIGH);
      digitalWrite(SEG_C, HIGH);
      break;
    case 8:
      digitalWrite(SEG_A, HIGH);
      digitalWrite(SEG_B, HIGH);
      digitalWrite(SEG_C, HIGH);
      digitalWrite(SEG_D, HIGH);
      digitalWrite(SEG_E, HIGH);
      digitalWrite(SEG_F, HIGH);
      digitalWrite(SEG_G, HIGH);
      break;
    case 9:
      digitalWrite(SEG_A, HIGH);
      digitalWrite(SEG_B, HIGH);
      digitalWrite(SEG_C, HIGH);
      digitalWrite(SEG_D, HIGH);
      digitalWrite(SEG_F, HIGH);
      digitalWrite(SEG_G, HIGH);
      break;
  }
}

void clearDisplay() {
  digitalWrite(SEG_A, LOW);
  digitalWrite(SEG_B, LOW);
  digitalWrite(SEG_C, LOW);
  digitalWrite(SEG_D, LOW);
  digitalWrite(SEG_E, LOW);
  digitalWrite(SEG_F, LOW);
  digitalWrite(SEG_G, LOW);
}

void moveServo(int count) {
  int angle = (count - 1) * 20;  // 20 degree increments
  servoMotor.write(angle);
}

void blinkLEDs(int count) {
  for (int i = 0; i < count; i++) {
    if (i % 2 == 0) {
      digitalWrite(LED_GREEN, HIGH);
      digitalWrite(LED_RED, LOW);
    } else {
      digitalWrite(LED_GREEN, LOW);
      digitalWrite(LED_RED, HIGH);
    }
    delay(200);
    digitalWrite(LED_GREEN, LOW);
    digitalWrite(LED_RED, LOW);
    delay(150);
  }
}