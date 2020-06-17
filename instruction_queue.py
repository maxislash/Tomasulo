import system
import adder

issue_stall = 0

def exe():
	global instruction, operand, dest, vj, vk, issue_stall

	if system.stall == 1 and issue_stall == 1 and system.busy_reg[int(dest[1])] == 0:
		issue_stall = 0
		system.stall = 0

	if len(system.inst_queue) == 0 and system.stall == 0:
		operand = 0
		dest = 0
		vj = 0
		vk = 0

	if len(system.inst_queue) > 0 and system.stall == 0:

		## Decoding next instruction and removing it from the queue
		instruction = system.inst_queue[0].split()
		operand = instruction[0]
		dest = instruction[1]
		vj = instruction[2]
		vk = instruction[3]

		if system.busy_reg[int(dest[1])] == 1:
			issue_stall = 1
			system.stall = 1

		else:
			system.inst_queue.pop(0)
			system.instruction_issued = 0
			system.busy_reg[int(dest[1])] = 1

	return operand, dest, vj, vk