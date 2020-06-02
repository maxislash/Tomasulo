from config import *

start_clock_add = [0]*add_number
add1 = [0]*add_number
add2 = [0]*add_number
op_add = [0]*add_number
busy_add = [0]*add_number
dest_add = ['0']*add_number

def adder(clock, number, op, v1, v2, dest):
	global start_clock_add, add1, add2, op_add, result_queue
	if op == "ADD" or op == "SUB":
		op_add[number] = op
		add1[number] = v1
		add2[number] = v2
		dest_add[number] = dest
		start_clock_add[number] = clock
		busy_add[number] = 1
		print("start", op, "on adder", number)

	elif op == 0 and clock == start_clock_add[number] + add_time and start_clock_add[number] != 0:
		if op_add[number] == "ADD":
			result_queue.append([dest_add[number], add1[number] + add2[number]])
			print("operation finished, send result", add1[number] + add2[number], "on result_queue from adder", number)
		elif op_add[number] == "SUB":
			result_queue.append([dest_add[number], add1[number] - add2[number]])
			print("operation finished, send result", add1[number] - add2[number], "on result_queue from adder", number)

		busy_add[number] = 0