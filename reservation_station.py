from config import *

def reservation_station_adder(number):

	global op_res_add, v1_add, v2_add, busy_res_add, v1_add_ready, v2_add_ready, operand, vj, vk, instruction_issued

	if busy_res_add[number] == 0 and (operand == "ADD" or operand == "SUB") and instruction_issued == 0:
		busy_res_add[number] = 1
		op_res_add[number] = operand
		v1_add[number] = vj
		v2_add[number] = vk

		if(vj[0] != 'R'):
			v1_add[number] = int(vj)
			v1_add_ready = 1
		else:
			v1_add[number] = vj
			reg_number = int[vj[1]]
			if busy_reg[reg_number] == 0 and empty_reg[reg_number] == 0:
				v1_add[number] = register[reg_number]
				v1_add_ready = 1
				
		if(vk[0] != 'R'):
			v2_add[number] = int(vk)
			v2_add_ready = 1
		else:
			v2_add[number] = vk
			reg_number = int[vk[1]]
			if busy_reg[reg_number] == 0 and empty_reg[reg_number] == 0:
				v2_add[number] = register[reg_number]
				v2_add_ready = 1

		instruction_issued = 1
		#print("instruction_issued")

		if v1_add_ready == 1 and v2_add_ready == 1:
			#adder(number, op_res_add[number], v1[number], v2[number])
			pass

	elif busy_res_add[number] == 1:
		pass

	
	print("reservation_station_adder number", number, ":" , "operand", op_res_add[number], "|",  v1[number], "|", v2[number])
	print()