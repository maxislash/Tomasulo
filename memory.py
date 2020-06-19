import system

global start_clock, dest, data, start, address, busy, inst
start = 0
start_clock = 0
inst = 0
dest = 0
address = 0
data = 0

def exe(instruction):

	global start_clock, dest, data, start, address, inst

	if (instruction[0] == "LD" or instruction[0] == "STR") and start == 1:
		system.stall["mem"] = 1

	if (instruction[0] == "LD" or instruction[0] == "STR") and start == 0:
		start_clock = system.clock
		inst = instruction[0]
		dest = instruction[1]
		system.busy_reg[int(dest[1])] = 1
		address = instruction[2]
		data = instruction[3]
		start = 1
		system.stall["mem"] = 0

		#system.inst_queue.pop(0)
		# print("start", inst, dest, address)

	elif system.clock == start_clock + system.load_time and start == 1:
		if inst == "LD":
			system.result_queue.append([dest, system.mem[int(address)]])
			# print("send", system.mem[int(address)], "to", dest)
		if inst == "STR":
			if dest != "0":
				system.mem[int(address)] = system.register[int(dest[1])]
				system.busy_reg[int(dest[1])] = 0
				# print("store", dest, "at memory address", address)
			else:
				system.mem[int(address)] = int(data)
				# print("store", data, "at memory address", address)

		start = 0
		

