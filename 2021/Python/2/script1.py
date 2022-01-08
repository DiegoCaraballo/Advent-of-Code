# --- Day 2: Dive! ---
# https://adventofcode.com/2021/day/2

def file_to_list(file):
    
    # Open file with inputs and create a list
    with open(file) as f:
        report_list = list(f.read().splitlines())
        
    return report_list

def calculate_position(report):
    horizontal_position = 0
    depth = 0
    
    for r in report:
        movement = r.split(' ')
        
        if movement[0] == 'forward':
            horizontal_position += int(movement[1])
        elif movement[0] == 'up':
            depth -= int(movement[1])
        elif movement[0] == 'down':
            depth += int(movement[1])
            
    return horizontal_position * depth

if __name__ == '__main__':
    data = file_to_list('input.txt')
    print(calculate_position(data))