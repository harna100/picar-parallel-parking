
# Setup
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 6
ECHO = 5

print "Distance measurement in progress"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)

print "Waiting for sensor to Settle"

time.sleep(2)

try:
	while True:
		# Send out a pulse
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		# Start the timer
		while GPIO.input(ECHO)==0:
			pulse_start = time.time()


		# Wait for the pulse to come back
		while GPIO.input(ECHO)==1:
			pulse_end = time.time()


		# Measure the difference
		pulse_duration = pulse_end - pulse_start


		# Calculate the distance
		distance = pulse_duration * 17150

		distance = round(distance, 2)

		print "Distance: " + str(distance) + "cm"

		time.sleep(1)	
except Exception as e:
	# Cleanup the pins
	GPIO.cleanup()

