global add_number
add_number = 3

def initialize():
	global clock
	clock = 1
	global max_time
	max_time = 8
	global sleep_duration 
	sleep_duration = 1

	global register 
	register = [0,0,0,0,0]
	global busy_reg
	busy_reg = [0,0,0,0,0]
	global empty_reg
	empty_reg = [1,1,1,1,1]

	global inst_queue
	inst_queue = ["ADD R0 1 2", "ADD R1 4 6", "ADD R2 R0 R1"]

	global result_queue
	result_queue = [[] for i in range(10)]
	result_queue.clear()

	global add_time
	add_time = 2

	global instruction_issued
	instruction_issued = 0

