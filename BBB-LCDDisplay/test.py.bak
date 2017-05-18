from servo import *
from i2c import *
from gpio import *

import time

def test_gpio():
	pin44 = BBB_GPIO("P8_44")
	pin44.direction(OUTPUT)
	pin44.value(HIGH)

def test_servo():
	servo = Servo()
	servo.polarity(1)
	servo.dutycicle(25)
	servo.frequence(100)
	servo.start()

def test_i2c():
	a = I2C(0x1D, 2)
	a.write('a')
	a.write(0x01)

def test_blinkled():
	pin44 = BBB_GPIO("P8_44")
	pin44.direction(OUTPUT)
	while True:
		pin44.value(HIGH)
		time.sleep(0.5)
		pin44.value(LOW)


if __name__ == '__main__':
	#test_gpio()
	#test_i2c()
	#test_servo()
	test_blinkled()
