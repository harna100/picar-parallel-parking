import time
import RPi.GPIO as GPIO

class MyUltrasonic(object):
	timeout = 0.05

	def __init__(self, echo, trig):
		self.echo = echo
		self.trig = trig
		GPIO.setmode(GPIO.BCM)

	def distance(self):
		GPIO.setup(self.trig, GPIO.OUT)
		GPIO.setup(self.echo, GPIO.IN)
		# Send out a pulse
		GPIO.output(self.trig, True)
		time.sleep(0.00001)
		GPIO.output(self.trig, False)

		# Start the timer
		while GPIO.input(self.echo)==0:
			pulse_start = time.time()


		# Wait for the pulse to come back
		while GPIO.input(self.echo)==1:
			pulse_end = time.time()


		# Measure the difference
		pulse_duration = pulse_end - pulse_start


		# Calculate the distance
		distance = pulse_duration * 17150

		return distance

	def getDistance(self, sampleSize=5):
		total = 0
		for i in range(sampleSize):
			a = self.distance()
			total += a
		return int(total/sampleSize)

	def less_than(self, alarm_gate):
		dis = self.get_distance()
		status = 0
		if dis >=0 and dis <= alarm_gate:
			status = 1
		elif dis > alarm_gate:
			status = 0
		else:
			status = -1
		return status