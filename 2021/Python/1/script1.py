# --- Day 1: Sonar Sweep ---
# https://adventofcode.com/2021/day/1

def count_measurement():
    
    # Open file with inputs and create a list
    with open('input.txt') as f:
        measurement_list = list(map(int, f.read().splitlines()))
        
    count = 0
    for idx, measurement in enumerate(measurement_list):
        if idx != 0 and measurement > measurement_list[idx-1]:
            count += 1
    return count

print(count_measurement())