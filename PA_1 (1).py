import random
import time
from tabulate import tabulate

def one_dimension(moves):
    counter = 0
    x = 0   
    for i in range(moves):  
        direction = random.choice(["Left", "Right"])
        if direction == "Left":
            x -= 1
        elif direction == "Right":
            x += 1
            if x == 0:
                counter += 1
                break
    return counter

def two_dimension(moves):
    counter = 0
    x = 0
    y = 0
    for i in range(moves):
        direction = random.choice(["Left", "Right", "Up", "Down"])
        if direction == "Left":
            x -= 1
        elif direction == "Right":
            x += 1
        if direction == "Up":
            y += 1
        elif direction == "Down":
            y -= 1
        if x == 0 and y == 0:
            counter += 1
            break        
    return counter 
            
def three_dimension(moves):
    counter = 0
    x = 0
    y = 0
    z = 0
    for i in range(moves):
        direction = random.choice(["Left", "Right", "Up", "Down", "Z_Up", "Z_down"])
        if direction == "Left":
            x -= 1
        elif direction == "Right":
            x += 1
        if direction == "Up":
            y += 1
        elif direction == "Down":
            y -= 1
        if direction == "Z_Up":
            z += 1
        elif direction == "Z_down":
            z -= 1
        if x == 0 and y == 0 and z == 0:
            counter += 1
            break        
    return counter 

def run_experiment(move_values):
    results_one_dimension = []
    results_two_dimension = []
    results_three_dimension = []
    run_times_3d = []

    for moves in move_values:
        final_count_1d = sum(one_dimension(moves) for i in range(100))
        final_count_2d = sum(two_dimension(moves) for i in range(100))
        start_time = time.time()
        final_count_3d = sum(three_dimension(moves) for i in range(100))
        end_time = time.time()
        run_time_3d = end_time - start_time
        run_times_3d.append(run_time_3d)
        
        results_one_dimension.append(final_count_1d)
        results_two_dimension.append(final_count_2d)
        results_three_dimension.append(final_count_3d)

    data = [
        ["1D"] + results_one_dimension,
        ["2D"] + results_two_dimension,
        ["3D"] + results_three_dimension,
        ["Run time (seconds)"] + [""] * len(move_values),
        ["Number of Steps"] + move_values
    ]

    
    data[3][1:] = run_times_3d

    headers = ["", "Percentage of times returned to origin"] + [""] * len(move_values)

    table = tabulate(data, headers, tablefmt="grid")

    print(table)

def main():
    move_values = [20, 200, 2000, 20000, 200000, 2000000]
    run_experiment(move_values)






