import system

global start_clock_add, add1, add2, op_add, busy_add, start_add, dest_add
start_clock_add = [0]*system.add_number
add1 = [0]*system.add_number
add2 = [0]*system.add_number
op_add = [0]*system.add_number
busy_add = [0]*system.add_number
start_add = [0]*system.add_number
dest_add = ['0']*system.add_number

def exe(number, op, v1, v2, dest):
	
	if op == "ADD" or op == "SUB": #Start the clock when adder gets new instruction
		op_add[number] = op
		add1[number] = v1
		add2[number] = v2
		dest_add[number] = dest
		start_clock_add[number] = system.clock
		start_add[number] = 1
		#print("start", op, "on adder", number)

	elif op == 0 and system.clock == start_clock_add[number] + system.add_time and start_clock_add[number] != 0: #Send the result on CDB when the "calculation" is done
		if op_add[number] == "ADD":
			system.result_queue.append([dest_add[number], add1[number] + add2[number]])
			#print("operation finished, send result", add1[number] + add2[number], "on result_queue from adder", number)
		elif op_add[number] == "SUB":
			system.result_queue.append([dest_add[number], add1[number] - add2[number]])
			#print("operation finished, send result", add1[number] - add2[number], "on result_queue from adder", number)

		busy_add[number] = 0 #Adder isn't busy anymore
		start_add[number] = 0