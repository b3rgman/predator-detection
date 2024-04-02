from gpiozero import MotionSensor, LED

pir = MotionSensor(4)
red = LED(17)
# yellow = LED(21)
# green = LED(20)

# red.blink()
# yellow.blink()
# green.blink()

while True:
	pir.wait_for_motion()
	print("Motion detected!!")
	red.blink()
