from gpiozero import MotionSensor, LED, Button
import pygame
import sys

OnState = True
buttonOn=Button(24)
buttonOff=Button(22)
pygame.init()
pir = MotionSensor(27)
yellow = LED(23)

while True:
  if OnState == True:
    yellow.on()
  if buttonOn.is_pressed:
    break

yellow.off()
print("Motion Detection running")
while True:
 if pir.wait_for_motion():
  print("Motion detected!!")
 #red.blink()
  pygame.mixer.music.load("/home/raspi/repos/predator-detection/mixkit-flock-of-wild-geese-20.wav")
  pygame.mixer.music.play()
  pygame.event.wait()
 if buttonOff.is_pressed:
   break
sys.exit(0)
