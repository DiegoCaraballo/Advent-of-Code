# --- Day 2: Dive! ---
# https://adventofcode.com/2021/day/2

from script1 import file_to_list

def calculate_position(report):
    horizontal_position = 0
    depth = 0
    aim = 0
    
    for r in report:
        movement = r.split(' ')
        
        if movement[0] == 'forward':
            horizontal_position += int(movement[1]) 
            if aim != 0:
                depth += int(movement[1]) * aim
        elif movement[0] == 'up':
            aim -= int(movement[1])
        elif movement[0] == 'down':
            aim += int(movement[1])
        
    return horizontal_position * depth

if __name__ == '__main__':
    data = file_to_list('input.txt')
    print(calculate_position(data))