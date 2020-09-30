import numpy as np
import os
import sys
from typing import Tuple


class KnapsackSolver(object):
    """
    Class to solve knapsack problem
    using genetic algorithm
    """
    def __init__(self, file_name):
        self.__parse_file(file_name)
    
    def __parse_file(self, file_name: str) -> None:
        """Parse file with input for knapsack problem"""
        file_handler = open(file_name, 'r')
        self.items_num, self.capacity = map(int, file_handler.readline().split())

        self.weights = np.zeros(self.items_num, np.float)
        self.costs = np.zeros(self.items_num, np.float)

        for i in range(self.items_num):
            weight, cost = map(np.float, file_handler.readline().split())
            self.weights[i] = weight; self.costs[i] = cost

        file_handler.close()

    def generate_population(self) -> None:
        """Create initial population"""
        self.population = np.eye(self.items_num, dtype=np.bool)
    
    def mutate(self, chromosome: np.ndarray) -> np.ndarray:
        """Swap two random genes"""
        mutage_change = 0.1 # 10%
        if np.random.rand() < mutage_change:
            f_index, s_index = np.random.randint(self.items_num, size=2)
            chromosome[[f_index, s_index]] = chromosome[[s_index, f_index]]
        return chromosome
    
    def local_improve(self, chromosome: np.ndarray) -> np.ndarray:
        """Set to True some random False genes"""
        weight = lambda x: np.sum(self.weights, where=x)
        mask = np.where(chromosome == False)[0]
        to_change = np.maximum(np.random.randint(2, 8), int(self.items_num * 0.01))
        #to_change = np.maximum(int(self.items_num * 0.01), 1)
        to_change = np.minimum(to_change, mask.size) # if there are elements to change

        for i in range(to_change):
            rnd_idx = np.random.choice(mask)
            chromosome[rnd_idx] = True
            if weight(chromosome) > self.capacity:
                chromosome[rnd_idx] = False
        
        return chromosome
    
    def crossover(self, *parents) -> np.ndarray:
        """Create new chromosome using parents"""
        child = np.zeros(self.items_num, np.bool)
        for i in range(self.items_num):
            parent_num = int(np.round(np.random.rand()))
            child[i] = parents[parent_num][i]
        return child
    
    def get_costs(self) -> np.ndarray:
        """Return costs of every element in population"""
        return np.array([np.sum(self.costs, where=x) for x in self.population])
    
    def is_valid(self, chromosome: np.ndarray) -> bool:
        """Check is chromosome valid"""
        weight = np.sum(self.weights, where=chromosome)
        return weight <= self.capacity and not any(np.equal(self.population,chromosome).all(1))
    
    def solve(self, iterations_number: int) -> Tuple[np.float, np.ndarray]:
        """
        Solve knapsack problem using iterations_number of iterations
        """
        population = self.generate_population()
        max_mask, max_cost = None, -1 # items set and cost of this set

        for _ in range(iterations_number):
            costs = self.get_costs()
            max_idx, min_idx = np.argmax(costs), np.argmin(costs)

            if costs[max_idx] > max_cost: # check is best solution found
                max_mask = np.copy(self.population[max_idx])
                max_cost = costs[max_idx]
            
            while (rand_idx := np.random.randint(self.items_num)) == max_idx: pass
            new_chromosome = self.crossover(self.population[max_idx], self.population[rand_idx])
            new_chromosome = self.mutate(new_chromosome)
            new_chromosome = self.local_improve(new_chromosome)

            if self.is_valid(new_chromosome):
                self.population[min_idx] = new_chromosome
            
        return max_mask, max_cost

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('Incorrect number of parameters!')
    if not sys.argv[2].isnumeric():
        sys.exit('Invalid number of iterations')
    if not os.path.exists(sys.argv[1]):
        sys.exit('Invalid path to file')
    
    solver = KnapsackSolver(sys.argv[1])
    mask, cost = solver.solve(int(sys.argv[2]))
    print(cost); print(np.where(mask)[0])