from vector import vector
import ast
import copy
import itertools

with open('bss_1.txt') as file:
    if file.readable():
        content = file.read()
        data_dict = ast.literal_eval(content)

        i = [vector(r, e, d) for r, e, d in zip(data_dict['r'], data_dict['e'], data_dict['d'])]
    else:
        print('scheiss datei')

def SJF_non_preemptive(i):
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

def preemptive_sjf(processes):
    c = 0
    R = 0
    n = len(processes)
    remaining_time = [p.getE() for p in processes]
    arrival_times = [p.getR() for p in processes]
    completed_processes = 0
    remaining_processes = n

    while remaining_processes > 0:
        # Find the process with the shortest remaining time at the current time
        smallest_remaining_time = float('inf')
        smallest_index = -1

        for i in range(n):
            if arrival_times[i] <= c and remaining_time[i] < smallest_remaining_time and remaining_time[i] > 0:
                smallest_remaining_time = remaining_time[i]
                smallest_index = i

        if smallest_index == -1:
            c += 1
            continue

        remaining_time[smallest_index] -= 1
        c += 1

        if remaining_time[smallest_index] == 0:
            completed_processes += 1
            remaining_processes -= 1
            R += (c - arrival_times[smallest_index] - processes[smallest_index].getE())

    R = R / n if n > 0 else 0
    return R

print("SFJ non_preemptive: ", SJF_non_preemptive(i),)
print("SFJ preemptive: ", preemptive_sjf(i),)

#permutation
def evaluate_permutations(original_processes, all_permutations):
    results = []

    for idx, perm in enumerate(all_permutations, start=1):
        # Create a copy of the original processes
        permuted_processes = copy.deepcopy(original_processes)
        
        # Assign the permuted execution times
        for process, new_e in zip(permuted_processes, perm):
            process.setE(new_e)
        
        # Evaluate the permutation using your scheduling algorithm
        # For demonstration, we use a placeholder function evaluate_processes
        avg_waiting_time = evaluate_processes(permuted_processes)
        
        results.append((idx, permuted_processes, avg_waiting_time))
        print(f'Permutation {idx}: Execution Times = {perm}, Average Waiting Time = {avg_waiting_time}')
    
    return results

def evaluate_processes(processes):
    return SJF_non_preemptive(processes)

# Example SJF_non_preemptive function for demonstration purposes
def SJF_non_preemptive(processes):
    processes.sort(key=lambda x: (x.getR(), x.getE()))  # Sort by arrival time, then by execution time
    current_time = 0
    waiting_time = 0
    completed_processes = 0
    n = len(processes)

    while processes:
        # Get processes that have arrived by current time
        ready_queue = [p for p in processes if p.getR() <= current_time]
        
        if ready_queue:
            # Sort ready queue by execution time to select the shortest job
            ready_queue.sort(key=lambda x: x.getE())
            current_process = ready_queue[0]
            processes.remove(current_process)
            arrival, execution, _ = current_process.get_values()
            
            # Calculate waiting time for the current process
            waiting_time += current_time - arrival
            
            # Execute the process
            current_time += execution
            completed_processes += 1
        else:
            # If no process is ready, move to the next arrival time
            current_time = processes[0].getR()
    
    average_waiting_time = waiting_time / n if n > 0 else 0
    return average_waiting_time

# Evaluate permutations
execution_times = [p.getE() for p in i]

# Generate all permutations of the execution times
all_permutations = list(itertools.permutations(execution_times))
results = evaluate_permutations(i, all_permutations)