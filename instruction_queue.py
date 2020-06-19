import system
import adder

issue_stall = 0

def exe():
	global instruction, operand, dest, vj, vk, issue_stall

	if system.stall["issue"] == 0 and system.stall["mem"] == 0 and system.stall["add"] == 0 and system.stall["mul"] == 0 and system.clock != 1 and len(system.inst_queue) != 0:
		system.inst_queue.pop(0)
		system.stall["general"] = 0

	if len(system.inst_queue) == 0:
		return 0, 0, 0, 0
	## Decoding next instruction and removing it from the queue
	instruction = system.inst_queue[0].split()
	operand = instruction[0]
	dest = instruction[1]
	vj = instruction[2]
	vk = instruction[3]

	# print(instruction)

	if system.busy_reg[int(dest[1])] == 1:
		system.stall["issue"] = 1
		operand = 0
		dest = 0
		vj = 0
		vk = 0

	else:
		system.stall["issue"] = 0

	if system.stall["issue"] == 1 or system.stall["mem"] == 1 or system.stall["add"] == 1 or system.stall["mul"] == 1:
		system.stall["general"] = 1

	else:
		system.instruction_issued = 0
	
	return operand, dest, vj, vk

	# else:
	# 	print("return 0")
	# 	return 0, 0, 0, 0



	