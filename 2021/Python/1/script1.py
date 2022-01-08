# --- Day 1: Sonar Sweep ---
# https://adventofcode.com/2021/day/1
import os

def file_to_list(file):

    # Open file with inputs and create a list
    with open(file) as f:
        report_list = list(map(int, f.read().splitlines()))
        
    return report_list

def count_measurement(report):
        
    count = 0
    for idx, measurement in enumerate(report):
        if idx != 0 and measurement > report[idx-1]:
            count += 1
    return count

# Test Script
if __name__ == '__main__':
    measurement_list = file_to_list('input.txt')
    print(count_measurement(measurement_list))