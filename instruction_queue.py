from config import *

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