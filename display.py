import system
import instruction_queue
import reservation_station
import adder
import multiplier
import cdb

def show():
	print("clock cycle: ", system.clock)

	if system.stall["general"] == 1:
		print("stall")

	# ##Instruction queue
	print("Instruction queue:", instruction_queue.operand, instruction_queue.dest, instruction_queue.vj, instruction_queue.vk)

	#Adder reservation station
	for i in range(system.add_number):
		print("reservation_station_adder", i,  "busy", adder.busy_add[i], "dest", reservation_station.dest_add[i], "operand", reservation_station.op_res_add[i], "v1", reservation_station.v1_add[i], "v2", reservation_station.v2_add[i])

	#Multiplier reservation station
	for i in range(system.mul_number):
		print("reservation_station_mul", i,  "busy", multiplier.busy_mul[i], "dest", reservation_station.dest_mul[i], "operand", reservation_station.op_res_mul[i], "v1", reservation_station.v1_mul[i], "v2", reservation_station.v2_mul[i])

	#If Adder starts a calculation or is done with it
	for i in range(system.add_number):
		if adder.start_add[i] == 1 and system.clock == adder.start_clock_add[i]:
			print("Adder", i, " has started operation", adder.op_add[i], adder.add1[i], adder.add2[i], " - dest", adder.dest_add[i], "sent on CDB")

		if adder.start_clock_add[i] != 0 and system.clock == (adder.start_clock_add[i] + system.add_time):
	 		print("Adder", i, " has finished operation", adder.op_add[i], adder.add1[i], adder.add2[i], " - dest", adder.dest_add[i], "sent on CDB")

	 #If Multiplier starts a calculation or is done with it
	for i in range(system.mul_number):
		if multiplier.start_mul[i] == 1 and system.clock == multiplier.start_clock_mul[i]:
			print("Multiplier", i, " has started operation", multiplier.op_mul[i], multiplier.mul1[i], multiplier.mul2[i], " - dest", multiplier.dest_mul[i], "sent on CDB")

		if multiplier.start_clock_mul[i] != 0 and system.clock == (multiplier.start_clock_mul[i] + system.mul_time):
	 		print("multiplier", i, " has finished operation", multiplier.op_mul[i], multiplier.mul1[i], multiplier.mul2[i], " - dest", multiplier.dest_mul[i], "sent on CDB")

	# Registers
	for i in range(len(system.register)):
		print("R", i, ": ", system.register[i], sep='')
	for i in range(len(system.register)):
		print("Busy R", i, ": ", system.busy_reg[i], sep='')
	# for i in range(len(system.register)):
	# 	print("Empty R", i, ":", system.empty_reg[i], sep='')

	print()