import system

global start_clock, dest, data, start, address, busy
start = 0
start_clock = 0
dest = 0
address = 0
data = 0

def exe(instruction):

	global start_clock, dest, data, start, address

	if instruction[0] == "LD" and start == 1:
		system.stall = 1

	if instruction[0] == "LD" and start == 0:
		start_clock = system.clock
		dest = instruction[1]
		address = instruction[2]
		start = 1
		system.stall = 0
		print("start LD", dest, address)

	elif system.clock == start_clock + system.load_time and start == 1:
		system.result_queue.append([dest, system.mem[int(address)]])
		start = 0
		print("send", system.mem[int(address)], "to", dest)

