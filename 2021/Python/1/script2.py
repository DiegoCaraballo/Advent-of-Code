# --- Day 1: Sonar Sweep ---
# https://adventofcode.com/2021/day/1

from script1 import count_measurement, file_to_list

def count_three_measurement(report):
    sum = sum_measurement(report)
    count = count_measurement(sum)
    
    return count

def sum_measurement(report):
    sum_measurement = []
    for idx, measurement in enumerate(report):
        try:
            sum = measurement + report[idx+1] + report[idx+2]
            sum_measurement.append(sum)
        except:
            break
    
    return sum_measurement

# Test Script
if __name__ == '__main__':
    measurement_list = file_to_list('input.txt')
    print(count_three_measurement(measurement_list))
