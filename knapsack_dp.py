import numpy as np
import sys

def parse_file(file_name):
    file_handler = open(file_name, 'r')
    items_num, badge_size = map(int, file_handler.readline().split())
    weights = np.zeros(items_num, np.int)
    costs = np.zeros(items_num, np.int)

    for i in range(items_num):
        weight, cost = map(np.int, file_handler.readline().split())
        weights[i] = weight; costs[i] = cost

    file_handler.close()
    return badge_size, weights, costs

def solve(badge_size, weights, costs):
    items_num = len(weights)
    badge = np.zeros( (items_num + 1, badge_size + 1), np.int_)
 
    for i in range(1, items_num + 1):
        for j in range(badge_size + 1):
                badge[i][j] = badge[i - 1][j]
                if j >= weights[i - 1]:
                    badge[i][j] = np.maximum(badge[i][j], badge[i - 1][j - weights[i - 1]] + costs[i - 1]) 

    return np.max(badge)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Incorrect number of parameters!')
    
    badge_size, weights, costs = parse_file(sys.argv[1])
    answer = solve(badge_size, weights, costs)
    print(answer)
                


