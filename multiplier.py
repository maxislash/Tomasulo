import system

global start_clock_mul, mul1, mul2, op_mul, busy_mul, start_mul, dest_mul
start_clock_mul = [0]*system.mul_number
mul1 = [0]*system.mul_number
mul2 = [0]*system.mul_number
op_mul = [0]*system.mul_number
busy_mul = [0]*system.mul_number
start_mul = [0]*system.mul_number
dest_mul = ['0']*system.mul_number

#Multiplier ALU
def exe(number, op, v1, v2, dest):
	
	if op == "MUL" or op == "DIV": #Check if it's a MUL or DIV operation and start the clock
		op_mul[number] = op
		mul1[number] = v1
		mul2[number] = v2
		dest_mul[number] = dest
		start_clock_mul[number] = system.clock
		start_mul[number] = 1
		#print("start", op, "on muler", number)

	elif op == 0 and system.clock == start_clock_mul[number] + system.mul_time and start_clock_mul[number] != 0: #Send the result on CDB after the "computing" time
		if op_mul[number] == "MUL":
			system.result_queue.append([dest_mul[number], mul1[number] * mul2[number]])
			#print("operation finished, send result", mul1[number] + mul2[number], "on result_queue from muler", number)
		elif op_mul[number] == "DIV":
			system.result_queue.append([dest_mul[number], mul1[number] / mul2[number]])
			#print("operation finished, send result", mul1[number] - mul2[number], "on result_queue from muler", number)

		busy_mul[number] = 0 #Multiplier isn't busy anymore
		start_mul[number] = 0