##Import
import time

from config import *
from instruction_queue import *
from reservation_station import *
from adder import *
from cdb import *

#operand = 0
#dest = 0
#vj = 0
#vk = 0

##Main loop
while (clock < max_time):

	print("clock cycle: ", clock)

	instruction_queue()

	# for i in range(add_number):
	# 	reservation_station_adder(i)

	# for i in range(add_number):
	# 	adder(clock, i, 0, 0, 0, 0)

	if clock == 1:
		adder(clock, 0, "ADD", 1, 2, "R0")
		adder(clock, 1, 0, 0, 0, 0)
		adder(clock, 2, 0, 0, 0, 0)
		v1_add[2] = "R0"

	elif clock == 2:
		adder(clock, 0, 0, 0, 0, 0)
		adder(clock, 1, "ADD", 4, 6, "R1")
		adder(clock, 2, 0, 0, 0, 0)

	else:
		for i in range(add_number):
			adder(clock, i, 0, 0, 0, 0)

	for i in range(len(result_queue)):
			print(result_queue[i])

	cdb()

	for i in range(5):
		print("Register", i, ":", register[i])

	for i in range(3):
		print("reservation_station_adder", i,  "v1", v1_add[i])


	## Next clock cycle
	clock += 1
	time.sleep(sleep_duration)

