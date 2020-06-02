clock = 1
max_time = 8
sleep_duration = 1

add_time = 2
add_number = 3

result_queue = [[] for i in range(10)]
result_queue.clear()

register = [0,0,0,0,0]
busy_reg = [0,0,0,0,0]
empty_reg = [0,0,0,0,0]

busy_res_add = [0]*add_number
op_res_add = [0]*add_number
v1_add = [0]*add_number
v2_add = [0]*add_number
v1_add_ready = [0]*add_number
v2_add_ready = [0]*add_number
instruction_issued = 0

inst_queue = ["ADD R0 1 2", "ADD R1 2 3", "MUL R2 R0 R1"]