#Parallel parking
from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
import time
import picar
from picar import front_wheels
from picar import back_wheels

picar.setup()

forward_speed = 20

fw = front_wheels.Front_Wheels(db = 'config')
bw = back_wheels.Back_Wheels(db='config')

#front ultrasonic sensor
UA1 = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)#change to appropriate pin
threshold = 10 #what is this

#to have it pull up to first cone

def pullUp():
    distance = UA1.get_distance()
    while (distance > 6):#move until the sensor senses something
        bw.forward()
        distance = UA1.get_distance()
    bw.stop()
    return True

def pullPast():
    distance = UA1.get_distance()
    while (distance <= 6):
        bw.forward()
        distance = UA1.get_distance()
    bw.stop()
    return True

def measureDistance():#supposing 0.1 second at speed 20 covers 2cm
    count = 0
    while True:
        distance = UA1.get_distance()
        if (distance > 6):
            bw.forward()
            time.sleep(0.1)
            count+=1
        else
            bw.stop()

        return (count*2)
    
def main():
    cont = pullUp()
    if cont == True:
        cont = pullPast()
        if cont = True:
            measureDistance()
        
        
