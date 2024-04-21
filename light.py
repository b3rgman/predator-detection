from gpiozero import LED, Button
from signal import pause
import sys
state = True
yellow = LED(23)
button = Button(24)

while(True):
  if state == True:
    yellow.on()
    button.wait_for_press()
    state = False
    yellow.off()
