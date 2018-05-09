"""
"Hello world" on Gemma

2018-0509 PePo 1ste version
TODO: use Gemma instead of Arduino Lilypad
"""
import board  # Gemma board specification
import digitalio # for digital IO
import time  # for sleep/delay

led = digitalio.DigitalInOut(board.D13) # builtin LED on board D13
led.direction = digitalio.Direction.OUTPUT # LED is output device

# run forever: turn LED on, turn LED off
while True:
  led.value=True
  time.sleep(0.1)
  led.value = False
  time.sleep(0.5)
