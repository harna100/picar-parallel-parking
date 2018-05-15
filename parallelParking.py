import picar
from picar import back_wheels
# from picar import front_wheels
import front_wheels
import MyUltrasonic
from time import sleep
# from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
import Ultrasonic_Avoidance
import math

def park(frontUA, backUA, frontWheels, backWheels):
	backWheels.backward()
	backWheels.speed = 30
	frontWheels.turn_right()
	sleep(2.3)
	frontWheels.turn_left()
	sleep(2)
	frontWheels.turn_straight()
	bw.speed = 0
	sleep(0.5)
	bw.speed = 20
	# sleep(0.7)
	timeElapsed = 0
	while True:
		dist = backUA.getDistance()
		if(dist > 70):
			continue
		if dist < 7 or timeElapsed >= 0.7:
			print(timeElapsed)
			print(dist)
			backWheels.forward()
			break
		sleep(0.05)
		timeElapsed += 0.05

	# sleep(0.8)
	timeElapsed = 0
	while True:
		dist = frontUA.get_distance()
		if dist < 7 or timeElapsed >= 0.8:
			print(timeElapsed)
			print(dist)
			break
		sleep(0.05)
		timeElapsed += 0.05


def makeEven(frontUA, backUA, frontWheels, backWheels):
	while True:
		frontDist = frontUA.get_distance()
		backDist = backUA.getDistance()
		difference = math.fabs(frontDist-backDist)
		if difference < 10:
			break
		if frontDist > backDist:
			backWheels.forward()
		elif backDist > frontDist:
			backWheels.backward()
		sleep(0.05)


#setup wheels
bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()

fw.turning_max = 40
fw.turning_offset = 40
fw.turn_straight()

bw.speed = 0
bw.forward()

#setup sensors
side = MyUltrasonic.MyUltrasonic(6,5)
back = MyUltrasonic.MyUltrasonic(19,13)
front = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)


state = 1
oldDistance = side.getDistance()
while state != 6:
	if state == 1: # sense first cone
		bw.speed = 25
		currDistance = side.getDistance()
		if currDistance > 150:
			continue
		if currDistance < 10:
			state = 2
			bw.speed = 0
			sleep(1)
			oldDistance = currDistance
		oldDistance = currDistance
		sleep(0.1)
	elif state == 2: # get past cone
		bw.speed = 25
		sleep(3)
		state = 3
		# currDistance = side.getDistance()
		# if currDistance > 150:
		# 	continue
		# if currDistance > 20:
		# 	state = 3
		# 	bw.speed = 0
		# 	sleep(1)
		# 	oldDistance = currDistance
		# oldDistance = currDistance
		# sleep(0.1)

	elif state == 3: # sense second cone
		bw.speed = 25
		currDistance = side.getDistance()
		if currDistance > 150:
			continue
		if currDistance < 20:
			state = 4
			sleep(0.5)
			bw.speed = 0
			sleep(1)
			oldDistance = currDistance
		oldDistance = currDistance
		sleep(0.1)
	elif state == 4: # back in
		park(front,back,fw,bw)
		state = 5

	elif state == 5: # make it even
		makeEven(front,back,fw,bw)
		state = 6
		break

bw.speed = 0