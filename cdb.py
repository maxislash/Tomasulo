import system
from reservation_station import v1_add, v2_add

global register
global v1_add, v2_add

def exe():

	for i in range(len(system.result_queue)):
		result = system.result_queue[0]
		register_number = int((result[0])[1])
		system.register[register_number] = result[1]
		system.busy_reg[register_number] = 0
		system.empty_reg[register_number] = 0

		for j in range(system.add_number):
			if v1_add[j] == result[0]:
				v1_add[j] = result[1]
				
			if v2_add[j] == result[0]:
				v2_add[j] = result[1]
				
		system.result_queue.pop(0)