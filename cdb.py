import system
from reservation_station import v1_add, v2_add, v1_mul, v2_mul

global register
global v1_add, v2_add, v1_mul, v2_mul

def exe():

	# Fetch the results on the result_queue and send them back to the registers as well as the reservation stations
	for i in range(len(system.result_queue)):
		result = system.result_queue[0]
		register_number = int((result[0])[1])
		system.register[register_number] = result[1] #Store the result in the register
		system.busy_reg[register_number] = 0
		system.empty_reg[register_number] = 0

		for j in range(system.add_number): #Check if the adder reservation station needs the results
			if v1_add[j] == result[0]:
				v1_add[j] = result[1]
				
			if v2_add[j] == result[0]:
				v2_add[j] = result[1]
				
		for j in range(system.mul_number): #Check if the multiplier reservation station needs the results
			if v1_mul[j] == result[0]:
				v1_mul[j] = result[1]
				
			if v2_mul[j] == result[0]:
				v2_mul[j] = result[1]

		system.result_queue.pop(0)