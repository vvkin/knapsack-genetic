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
        objects_num = int(sys.argv[1])
        badge_capacity = float(sys.argv[2])
        values_type = lambda x: (round(x) if sys.argv[3] == 'int' else float(x))
        badge_capacity = values_type(badge_capacity)
        max_weight, max_cost = map(float, sys.argv[4:6])
        max_weight, max_cost = max(1, max_weight), max(max_cost, 2)
        file_name = sys.argv[-1]
        with open(file_name, 'w') as file_handler:
            file_handler.write(f'{objects_num} {badge_capacity}\n')
            for _ in range(objects_num):
                current_weight = values_type(random.uniform(1, max_weight)) # only non zero values
                current_cost = values_type(random.uniform(2, max_cost)) # values bigger than 2
                file_handler.write(f'{current_weight} {current_cost}\n')
    except Exception: 
        sys.exit('Sorry, but something went wrong')
