from gpiozero import MotionSensor, LED, Button
import pygame

button = Button(24)
pygame.init()
#pir = MotionSensor(4)
# yellow = LED(21)


button.wait_for_press()
pygame.mixer.music.load("mixkit-flock-of-wild-geese-20.wav")
pygame.mixer.music.play()
pygame.event.wait()
# print("Button was pressed")

# while True:
# 	if button.is_pressed:
#		print("Button was pressed")
#	else:
 #		print("Button was not pressed")


	# pir.wait_for_motion()
	#print("Motion detected!!")
	#red.blink()
	#pygame.mixer.music.load("mixkit-flock-of-wild-geese-20.wav")
	#pygame.mixer.music.play()
	#pygame.event.wait()
