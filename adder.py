# ##Import
# import time

from config import *

# ##Constants
# clock = 1
# max_time = 8
# sleep_duration = 1

# add_time = 2
# add_number = 3

start_clock_add = [0]*add_number
add1 = [0]*add_number
add2 = [0]*add_number
op_add = [0]*add_number
busy_add = [0]*add_number

def adder(clock, number, op, v1, v2):
	global start_clock_add, add1, add2, op_add
	if op == "ADD" or op == "SUB":
		op_add[number] = op
		add1[number] = v1
		add2[number] = v2
		start_clock_add[number] = clock
		busy_add[number] = 1
		print("start", op, "on adder", number)

	elif op == 0 and clock == start_clock_add[number] + add_time and start_clock_add[number] != 0:
		#cbd(op, number, v1 + v2)
		if op_add[number] == "ADD":
			print("operation finished, send result", add1[number] + add2[number], "on CBD from adder", number)
		elif op_add[number] == "SUB":
			print("operation finished, send result", add1[number] - add2[number], "on CBD from adder", number)

		busy_add[number] = 0

# ##Main loop
# while (clock < max_time):

# 	print("clock cycle: ", clock)

# 	if(clock == 1):
# 		adder(0, "ADD", 1, 2)
# 		adder(1, 0, 0, 0)
# 		adder(2, 0, 0, 0)

# 	if (clock == 2):
# 		adder(0, 0, 0, 0)
# 		adder(1, "ADD", 4, 6)
# 		adder(2, 0, 0, 0)

# 	if (clock > 2):
# 		for i in range(add_number):
# 			adder(i, 0, 0, 0)

# 	## Next clock cycle
# 	clock += 1
# 	time.sleep(sleep_duration)

