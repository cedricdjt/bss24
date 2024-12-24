import ast
from vector import vector
from collections import deque
import copy
import itertools

with open('bss_1.txt') as file:
    if file.readable():
        content = file.read()
        data_dict = ast.literal_eval(content)

        i = [vector(r, e, d) for r, e, d in zip(data_dict['r'], data_dict['e'], data_dict['d'])]
    else:
        print('scheiss datei')

# aufgabe 1
def FCFS(i):
    R = 0
    s = 0
    c = 0
    for process in i:
        r, e, d = process.get_values()
        s = c
        c = s + e
        if r < d:
            R += c
        else:
            print('deadline erreicht')
    R = R / len(i)
    return R


def SJF(i):
    R = 0
    s = 0
    c = 0
    sorted_process = sorted(i, key=lambda x: x.getE())  # x.getE() -< execution time
    for process in sorted_process:
        r, e, d = process.get_values()
        s = c
        c = s + e
        if R < d:
            R += c
        else:
            print('deadline erreicht')
    R = R / len(i)
    return R


def EDF(i):
    R = 0
    s = 0
    c = 0
    sorted_process = sorted(i, key=lambda x: x.getD())  # x.getD() -< deadline
    for process in sorted_process:
        r, e, d = process.get_values()
        s = c
        c = s + e
        if R < d:
            R += c
        else:
            print('deadline erreicht')
    R = R / len(i)
    return R


def LLF_non_preemptive(processes):
    time_quantum = 3
    R = 0  # Total completion time
    c = 0  # Current time
    queue = deque(sorted(processes, key=lambda p: p.getR()))  # Initialize queue sorted by arrival time
    ready_queue = deque()
    completed = 0
    n = len(processes)

    while queue or ready_queue:
        # Move processes that have arrived to the ready queue
        while queue and queue[0].getR() <= c:
            ready_queue.append(queue.popleft())

        if ready_queue:
            current_process = ready_queue.popleft()
            r, e, d = current_process.get_values()

            if e > time_quantum:
                # Execute for the time quantum
                c += time_quantum
                e -= time_quantum
                current_process.setE(e)  # Update remaining execution time
                # Reappend the process to the end of the ready queue
                ready_queue.append(current_process)
            else:
                # Execute the remaining time
                c += e
                e = 0
                R += c  # Add completion time

                if c > d:
                    print(f'Process with deadline {d} missed its deadline at time {c}.')
                completed += 1
        else:
            # If no process is ready, jump to the next process arrival time
            if queue:
                c = queue[0].getR()
            else:
                break

    average_completion_time = R / n if n > 0 else 0
    return average_completion_time


def RR(processes, time_quantum=3):
    R = 0  # Total completion time
    c = 0  # Current time
    queue = deque(sorted(processes, key=lambda p: p.getR()))  # Initialize queue sorted by arrival time
    ready_queue = deque()
    completed = 0
    n = len(processes)

    while queue or ready_queue:
        # Move processes that have arrived to the ready queue
        while queue and queue[0].getR() <= c:
            ready_queue.append(queue.popleft())

        if ready_queue:
            process = ready_queue.popleft()
            r, e, d = process.get_values()

            if e > time_quantum:
                # Execute for the time quantum
                c += time_quantum
                e -= time_quantum
                # Reappend the process with updated execution time
                process.setE(e)  # Update remaining execution time
                ready_queue.append(process)
            else:
                # Execute the remaining time
                c += e
                e = 0
                completed += 1
                R += c  # Add completion time

                if c > d:
                    print(f'Process with deadline {d} missed its deadline at time {c}.')
        else:
            # If no process is ready, jump to the next process arrival time
            if queue:
                c = queue[0].getR()
            else:
                break

    average_completion_time = R / n
    return average_completion_time


original_i = copy.deepcopy(i)

print('SJF:', SJF(i))
i = copy.deepcopy(original_i)

print('FCFS:', FCFS(i))
i = copy.deepcopy(original_i)

print('EDF: ', EDF(i))
i = copy.deepcopy(original_i)

print('LLF: ', LLF_non_preemptive(i))
i = copy.deepcopy(original_i)

print('RR: ', RR(i))
i = copy.deepcopy(original_i)


# permutation, aufgabe 2:
all_permutations = list(itertools.permutations(original_i))


for idx, permutation in enumerate(all_permutations, start=1):
    permutation_copy = copy.deepcopy(permutation)
    permutation_list = list(permutation_copy)
    R = RR(permutation_list)
    print(f'Permutation {idx}: RR = {R}')


# aufgabe 2: