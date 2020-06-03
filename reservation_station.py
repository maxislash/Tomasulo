import system
import adder

global busy_res_add, op_res_add, v1_add, v2_add, dest_add, launched_add

busy_res_add = [0]*system.add_number
op_res_add = [0]*system.add_number
v1_add = [0]*system.add_number
v2_add = [0]*system.add_number
dest_add = [0]*system.add_number
launched_add = [0]*system.add_number

def add_exe(number, instruction):
	if busy_res_add[number] == 0 and (instruction[0] == "ADD" or instruction[0] == "SUB") and system.instruction_issued == 0:

		busy_res_add[number] = 1
		launched_add[number] = 0
		op_res_add[number] = instruction[0]
		dest_add[number] = instruction[1]
		v1_add[number] = instruction[2]
		v2_add[number] = instruction[3]

		if(v1_add[number][0] != 'R'):
			v1_add[number] = int(v1_add[number])	
		else:
			reg_number = int(v1_add[number][1])
			if system.busy_reg[reg_number] == 0 and system.empty_reg[reg_number] == 0:
				v1_add[number] = system.register[reg_number]
		
		if(v2_add[number][0] != 'R'):
			v2_add[number] = int(v2_add[number])
		else:
			reg_number = int(v2_add[number][1])
			if system.busy_reg[reg_number] == 0 and system.empty_reg[reg_number] == 0:
				v2_add[number] = system.register[reg_number]

		system.instruction_issued = 1			

	if busy_res_add[number] == 1 and launched_add[number] == 0:
		if isinstance(v1_add[number], int) and isinstance(v2_add[number], int):
			adder.exe(number, op_res_add[number], v1_add[number], v2_add[number], dest_add[number])
			launched_add[number] = 1

		#print(number, op_res_add[number], v1_add[number], v2_add[number], dest_add[number])
	
	