##Import
import time
import display

import system
import instruction_queue
import memory
import reservation_station
import adder
import multiplier
import cdb

system.initialize()

##Main loop
for system.clock in range(1,system.max_time): #Clock cycle, every iteration is the following clock cycle
	
	instruction = instruction_queue.exe() #IF/ID (instruction fetch and decode)

	memory.exe(instruction) #Memory block, if the instruction is a load or store, it will be processed here

	for i in range(system.add_number): ##Adder reservation stations, send the instruction to the adder reservations stations
	 	reservation_station.add_exe(i, instruction)
	 	adder.exe(i, 0, 0, 0, 0)

	for i in range(system.mul_number):##Multiplier reservation stations, send the instruction to the multiplier reservations stations
		reservation_station.mul_exe(i, instruction)
		multiplier.exe(i, 0, 0, 0, 0)


	cdb.exe() ##Common Data Bus, which will broadcast the result back to the registers and reservation stations

	display.show() ##Will print the state of the machine

	## Next clock cycle
	time.sleep(system.sleep_duration)

for i in range(len(system.mem)):
	print("Memory slot", i, ": ", system.mem[i], sep='')

