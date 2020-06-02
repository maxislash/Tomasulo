from config import *

#def cdb(register,v1_add,v2_add, v1_add_ready, v2_add_ready):
def cdb():
	global result_queue, v1_add, v2_add, v1_add_ready, v2_add_ready, register

	for i in range(len(result_queue)):
		result = result_queue[0]
		register_number = int((result[0])[1])
		register[register_number] = result[1]
		busy_reg[register_number] = 0
		empty_reg[register_number] = 0

		for j in range(add_number):
			if v1_add[j] == result[0]:
				v1_add[j] = result[1]
				v1_add_ready = 1
			if v2_add[j] == result[0]:
				v2_add[j] = result[1]
				v2_add_ready = 1

		result_queue.pop(0)