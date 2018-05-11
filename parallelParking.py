import picar
from picar import back_wheels
# from picar import front_wheels
import front_wheels
import MyUltrasonic
from time import sleep
# from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
import Ultrasonic_Avoidance
import math

def park():
	bw.backward()
	bw.speed = 30
	fw.turn_right()
	sleep(2.3)
	fw.turn_left()
	sleep(2)
	fw.turn_straight()
	sleep(0.7)
	bw.forward()
	sleep(0.8)
	bw.speed = 0


#setup wheels
bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()

fw.turning_max = 40
fw.turning_offset = 30
fw.turn_straight()

bw.speed = 0
bw.forward()

#setup sensors
side = MyUltrasonic.MyUltrasonic(6,5)
back = MyUltrasonic.MyUltrasonic(19,13)
front = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)


state = 1
oldDistance = side.getDistance()
while state != 5:
	if state == 1: # sense first cone
		bw.speed = 20
		currDistance = side.getDistance()
		if currDistance > 150:
			continue
		if math.fabs(currDistance - oldDistance) > 20:
			state = 2
			bw.speed = 0
			sleep(2)
		oldDistance = currDistance
		sleep(0.1)
	elif state == 2: # get past cone
		bw.speed = 20
		currDistance = side.getDistance()
		if currDistance > 150:
			continue
		if math.fabs(currDistance - oldDistance) > 20:
			state = 3
			bw.speed = 0
			sleep(2)
		oldDistance = currDistance
		sleep(0.1)

	elif state == 3: # sense second cone
		bw.speed = 20
		currDistance = side.getDistance()
		if currDistance > 150:
			continue
		if math.fabs(currDistance - oldDistance) > 20:
			state = 4
			bw.speed = 0
			sleep(2)
		oldDistance = currDistance
		sleep(0.1)
	elif state == 4: # back in
		park()
		
	elif state == 5: # make it even
		break