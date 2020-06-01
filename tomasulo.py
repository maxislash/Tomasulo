##Import
import time
from adder import *
from config import *

# ##Constants
# clock = 1
# max_time = 4
# sleep_duration = 1

# add_time = 2
# add_number = 3

busy_res_add = [0]*add_number
op_res_add = [0]*add_number
v1 = [0]*add_number
v2 = [0]*add_number
instruction_issued = 0

inst_queue = ["ADD R0 1 2", "ADD R1 2 3", "MUL R2 R0 R1"]
register = [0,0,0,0,0]
busy_reg = [0,0,0,0,0]
empty_reg = [0,0,0,0,0]

operand = 0
dest = 0
#vj = 0
vk = 0

##Achitecture element
def instruction_queue():

	if len(inst_queue) > 0:
		print("instruction: ", inst_queue[0])

		## Decoding next instruction and removing it from the queue
		global instruction, operand, dest, vj, vk, instruction_issued
		instruction = inst_queue[0].split()
		operand = instruction[0]
		dest = instruction[1]
		vj = instruction[2]
		vk = instruction[3]
		instruction_issued = 0
		inst_queue.pop(0)

	else:
		operand = 0
		dest = 0
		vj = '0'
		vk = '0'

	return operand, dest, vj, vk

# start_clock_add = [0]*add_number
# add1 = [0]*add_number
# add2 = [0]*add_number
# op_add = [0]*add_number
# busy_add = [0]*add_number

# def adder(number, op, v1, v2):
# 	global start_clock_add, add1, add2, op_add
# 	if op == "ADD" or op == "SUB":
# 		op_add[number] = op
# 		add1[number] = v1
# 		add2[number] = v2
# 		start_clock_add[number] = clock
# 		busy_add[number] = 1
# 		print("start", op, "on adder", number)

# 	elif op == 0 and clock == start_clock_add[number] + add_time and start_clock_add[number] != 0:
# 		#cbd(op, number, v1 + v2)
# 		if op_add[number] == "ADD":
# 			print("operation finished, send result", add1[number] + add2[number], "on CBD from adder", number)
# 		elif op_add[number] == "SUB":
# 			print("operation finished, send result", add1[number] - add2[number], "on CBD from adder", number)

# 		busy_add[number] = 0

def reservation_station_adder(number):

	global op_res_add, v1, v2, busy_res_add, v1_ready, v2_ready, operand, vj, vk, instruction_issued

	if busy_res_add[number] == 0 and (operand == "ADD" or operand == "SUB") and instruction_issued == 0:
		busy_res_add[number] = 1
		op_res_add[number] = operand
		v1[number] = vj
		v2[number] = vk

		if(vj[0] != 'R'):
			v1[number] = int(vj)
			v1_ready = 1
		else:
			v1[number] = vj
			reg_number = int[vj[1]]
			if busy_reg[reg_number] == 0 and empty_reg[reg_number] == 0:
				v1[number] = register[reg_number]
				v1_ready = 1
				
		if(vk[0] != 'R'):
			v2[number] = int(vk)
			v2_ready = 1
		else:
			v2[number] = vk
			reg_number = int[vk[1]]
			if busy_reg[reg_number] == 0 and empty_reg[reg_number] == 0:
				v2[number] = register[reg_number]
				v2_ready = 1

		instruction_issued = 1
		#print("instruction_issued")

		if v1_ready == 1 and v2_ready == 1:
			#adder(number, op_res_add[number], v1[number], v2[number])
			pass

	elif busy_res_add[number] == 1:
		pass

	
	print("reservation_station_adder number", number, ":" , "operand", op_res_add[number], "|",  v1[number], "|", v2[number])
	print()

##Main loop
while (clock < max_time):

	print("clock cycle: ", clock)

	instruction_queue()

	# for i in range(add_number):
	# 	reservation_station_adder(i)

	if(clock == 1):
		adder(clock, 0, "ADD", 1, 2)
		adder(clock, 0, 0, 0, 0)
		adder(clock, 2, 0, 0, 0)

	if (clock == 2):
		adder(clock, 0, 0, 0, 0)
		adder(clock, 1, "ADD", 4, 6)
		adder(clock, 2, 0, 0, 0)

	if (clock > 2):
		for i in range(add_number):
			adder(clock, i, 0, 0, 0)

	## Next clock cycle
	clock += 1
	time.sleep(sleep_duration)

