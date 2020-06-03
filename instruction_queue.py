import system

def exe():
	
	if len(system.inst_queue) > 0:

		## Decoding next instruction and removing it from the queue
		instruction = system.inst_queue[0].split()
		operand = instruction[0]
		dest = instruction[1]
		vj = instruction[2]
		vk = instruction[3]
		system.inst_queue.pop(0)

		system.instruction_issued = 0
		system.busy_reg[int(dest[1])] = 1

	else:
		operand = 0
		dest = 0
		vj = '0'
		vk = '0'

	return operand, dest, vj, vk