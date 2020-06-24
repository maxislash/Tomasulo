import system
import adder
import multiplier

global op_res_add, v1_add, v2_add, dest_add 

op_res_add = [0]*system.add_number
v1_add = [0]*system.add_number
v2_add = [0]*system.add_number
dest_add = [0]*system.add_number

def add_exe(number, instruction):

	#print("reservation station number", number, "parse instruction", instruction, "busy", adder.busy_add[number], "issued", system.instruction_issued)

	if adder.busy_add[number] == 1 and adder.start_add[number] == 0: ##If the instruction has been registered by the reservation station but not yet started on the ALU because one data was missing
		if isinstance(v1_add[number], int) and isinstance(v2_add[number], int): ##Check if we have all the data needed now, if yes, start the ALU
			adder.exe(number, op_res_add[number], v1_add[number], v2_add[number], dest_add[number])

		#print(number, op_res_add[number], v1_add[number], v2_add[number], dest_add[number])

	if adder.busy_add[number] == 0 and (instruction[0] == "ADD" or instruction[0] == "SUB") and system.instruction_issued == 0: ##If we get an instruction from IF/ID and the reservation station isn't already busy

		adder.busy_add[number] = 1 ##Mark the reservation station has busy and keep the instruction
		op_res_add[number] = instruction[0]
		dest_add[number] = instruction[1]
		system.busy_reg[int(dest_add[number][1])] = 1
		v1_add[number] = instruction[2]
		v2_add[number] = instruction[3]

		if(v1_add[number][0] != 'R'): ##If first operand is immediate, store it in the reservation station
			v1_add[number] = int(v1_add[number])	
		else: ##Otherwise, check if the register wanted has a value and isn't being used
			reg_number = int(v1_add[number][1])
			if system.busy_reg[reg_number] == 0 and system.empty_reg[reg_number] == 0:
				v1_add[number] = system.register[reg_number]
		
		if(v2_add[number][0] != 'R'): #Same for second operand
			v2_add[number] = int(v2_add[number])
		else:
			reg_number = int(v2_add[number][1])
			if system.busy_reg[reg_number] == 0 and system.empty_reg[reg_number] == 0:
				v2_add[number] = system.register[reg_number]

		system.instruction_issued = 1 ##Instruction was registered by the reservation station
		system.stall["add"] = 0
		#system.inst_queue.pop(0)	

		print("instruction", instruction, "issued to reservation station", number)		

	if number == system.add_number-1 and system.instruction_issued == 0 and (instruction[0] == "ADD" or instruction[0] == "SUB"):## If all the reservation station are busy, stall
		system.stall["add"] = 1


global op_res_mul, v1_mul, v2_mul, dest_mul

op_res_mul = [0]*system.mul_number
v1_mul = [0]*system.mul_number
v2_mul = [0]*system.mul_number
dest_mul = [0]*system.mul_number

	
def mul_exe(number, instruction):

	if multiplier.busy_mul[number] == 1 and multiplier.start_mul[number] == 0:
		if isinstance(v1_mul[number], int) and isinstance(v2_mul[number], int):
			multiplier.exe(number, op_res_mul[number], v1_mul[number], v2_mul[number], dest_mul[number])

		#print(number, op_res_add[number], v1_add[number], v2_add[number], dest_add[number])

	if multiplier.busy_mul[number] == 0 and (instruction[0] == "MUL" or instruction[0] == "DIV") and system.instruction_issued == 0:

		multiplier.busy_mul[number] = 1
		op_res_mul[number] = instruction[0]
		dest_mul[number] = instruction[1]
		system.busy_reg[int(dest_mul[number][1])] = 1
		v1_mul[number] = instruction[2]
		v2_mul[number] = instruction[3]

		if(v1_mul[number][0] != 'R'):
			v1_mul[number] = int(v1_mul[number])	
		else:
			reg_number = int(v1_mul[number][1])
			if system.busy_reg[reg_number] == 0 and system.empty_reg[reg_number] == 0:
				v1_mul[number] = system.register[reg_number]
		
		if(v2_mul[number][0] != 'R'):
			v2_mul[number] = int(v2_mul[number])
		else:
			reg_number = int(v2_mul[number][1])
			if system.busy_reg[reg_number] == 0 and system.empty_reg[reg_number] == 0:
				v2_mul[number] = system.register[reg_number]

		system.instruction_issued = 1
		system.stall["mul"] = 0
		#system.inst_queue.pop(0)	

		#print("instruction", instruction, "issued to reservation station", number)		

	if number == system.add_number-1 and system.instruction_issued == 0 and (instruction[0] == "MUL" or instruction[0] == "DIV"):
		system.stall["mul"] = 1