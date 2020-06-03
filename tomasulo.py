##Import
import time

import system
import instruction_queue
import reservation_station
import adder
import cdb

system.initialize()

##Main loop
while (system.clock < system.max_time):

	print("clock cycle: ", system.clock)

	instruction = instruction_queue.exe()

	print(instruction)

	for i in range(system.add_number):
	 	reservation_station.add_exe(i, instruction)

	for i in range(system.add_number):
		adder.exe(i, 0, 0, 0, 0)

	# for i in range(len(system.result_queue)):
	# 		print(system.result_queue[i])

	cdb.exe()

	for i in range(5):
		print("Register", i, ":", system.register[i])
	for i in range(5):
		print("Busy Register", i, ":", system.busy_reg[i])
	# for i in range(5):
	# 	print("empty Register", i, ":", system.empty_reg[i])

	for i in range(3):
		print("reservation_station_adder", i,  "v1", reservation_station.v1_add[i], "v2", reservation_station.v2_add[i])


	## Next clock cycle
	system.clock += 1
	time.sleep(system.sleep_duration)