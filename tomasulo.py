##Import
import time
import display

import system
import instruction_queue
import reservation_station
import adder
import cdb

system.initialize()

##Main loop
for system.clock in range(1,system.max_time):
	
	instruction = instruction_queue.exe()

	for i in range(system.add_number):
	 	reservation_station.add_exe(i, instruction)
	 	adder.exe(i, 0, 0, 0, 0)

	cdb.exe()

	display.show()

	## Next clock cycle
	time.sleep(system.sleep_duration)