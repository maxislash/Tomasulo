global add_number
add_number = 3

global mul_number
mul_number = 2

def initialize():
	global clock
	clock = 1
	global max_time
	#max_time = 26
	max_time = 30
	global sleep_duration 
	sleep_duration = 1

	global register 
	register = [0,0,0,0,0]
	global busy_reg
	busy_reg = [0,0,0,0,0]
	global empty_reg
	empty_reg = [1,1,1,1,1]

	global mem
	mem = [10,20,30,40,50,60,70,80,90,100]

	global inst_queue
	inst_queue = ["ADD R0 1 2", "ADD R1 R0 7", "ADD R2 2 2", "SUB R3 R2 1", "ADD R4 5 16", "ADD R4 R1 R3", "MUL R0 5 6", "LD R1 1 0", "ADD R2 R0 R1", "STR R2 0 0"]
	#inst_queue = ["ADD R0 1 2", "LD R1 1 0", "LD R2 4 0"]

	global load_time
	load_time = 2

	global result_queue
	result_queue = [[] for i in range(10)]
	result_queue.clear()

	global add_time
	add_time = 2


	global mul_time
	mul_time = 10

	global instruction_issued
	instruction_issued = 0

	global stall
	stall = { "general": 0,
  			  "issue": 0,
  			  "mem": 0,
  			  "add": 0,
  			  "mul": 0 }
	#general, issue, memory, adder, multiplier

