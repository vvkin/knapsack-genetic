#!/usr/bin/env python

import random
import sys


"""
Usage:
python generate_data [object_num] [badge_volume] [values_type] [max_weight] [max_cost] [to_file] 
"""

if __name__ == '__main__':
    if len(sys.argv) != 7:
        sys.exit('Incorrect number of args')
    try:
        objects_num, badge_volume = map(int, sys.argv[1:3]) 
        values_type = int if sys.argv[3] == 'int' else float
        max_weight, max_cost = map(values_type, sys.argv[4:6])
        max_weight, max_cost = max(1, max_weight), max(max_cost, 2)
        file_name = sys.argv[-1]
        with open(file_name, 'w') as file_handler:
            file_handler.write(f'{objects_num} {badge_volume}\n')
            for _ in range(objects_num):
                current_weight = values_type(random.random() * max_weight) % (max_weight) + 1 # only non zero values
                current_cost = values_type(random.random() * max_cost) % (max_cost - 1) + 2  # values bigger than 2
                file_handler.write(f'{current_weight} {current_cost}\n')
    except Exception: 
        sys.exit('Sorry, but something went wrong')
