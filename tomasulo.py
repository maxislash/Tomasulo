##Import
import time

##Constants
clock = 1
max_time = 20
sleep_duration = 1

add_time = 2
add_number = 3

global busy_add 
busy_add = [0]*add_number
global op_add
op_add = [0]*add_number
global v1
v1 = [0]*add_number
global v2
v2 = [0]*add_number


inst_queue = ["ADD R0 1 2", "ADD R1 2 3", "MUL R2 R0 R1"]
register = [0,0,0,0,0]

operand = 0
dest = 0
#vj = 0
vk = 0

##Achitecture element
def instruction_queue():

	if len(inst_queue) > 0:
		print("instruction: ", inst_queue[0])

		## Decoding next instruction and removing it from the queue
		global instruction, operand, dest, vj, vk
		instruction = inst_queue[0].split()
		operand = instruction[0]
		dest = instruction[1]
		vj = instruction[2]
		vk = instruction[3]
		inst_queue.pop(0)

	else:
		operand = 0
		dest = 0
		vj = '0'
		vk = 0

	return operand, dest, vj, vk

def reservation_station_adder(number):
	if busy_add[number] == 0 and (operand == "ADD" or operand == "SUB"):
		busy_add[number] = 1
		op = operand
		v1 = vj
		v2 = vk

		#if empty[number] == 0

	elif busy_add[number] == 1:
		print()



##Main loop
while (clock < max_time):

	print("clock cycle: ", clock)

	instruction_queue()

	for i in range(add_number):
		reservation_station_adder(i)

	if(vj[0] != 'R'):
		v1 = int(vj)
	else:
		v1 = vj

	print(v1)
	print(type(v1))

	## Next clock cycle
	clock += 1
	time.sleep(sleep_duration)

