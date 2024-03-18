from typing import List


def scheduler(n: int, schedules: List[str]):
    func_schedules = dict()
    for i in range(n):
        func_schedules[str(i)] = []
    stack = []
    for log in schedules:
        [id, op, time] = log.split(":")
        if op == "start":
            if len(stack) == 0:
                stack.append(id)
                func_schedules[id].append([int(time), None])
            else:
                top = stack[-1]
                prev_func = func_schedules[top][-1]
                prev_func[1] = int(time) - 1
                func_schedules[id].append([int(time), None])
                stack.append(id)
        else:
            executing_func_id = stack.pop()
            schedule = func_schedules[executing_func_id][-1]
            schedule[1] = int(time)
            if len(stack) != 0:
                current_func = stack[-1]
                func_schedules[current_func].append([int(time) + 1, None])

    print(func_schedules)


scheduler(3, ["0:start:0", "2:start:4", "2:end:5", "1:start:7", "1:end:10", "0:end:11"])
