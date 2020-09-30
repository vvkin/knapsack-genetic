# Genetic algorithm (Knapsack problem)
Simple python script to solve **Knapsack problem** (heuristic). Dynamic programming implementation to check solution precision (integers only) 
## Dependecies
* `numpy`
## Get started
* `git clone https://github.com/vvkin/knapsack-genetic/`
* `cd knapsack-genetic`
* `pipenv install`
* `pipenv shell`
* `pytnon generate data.py 100 100 int 50 50 data`
* `python knapsack_genetic.py data 10000`
## Usage
### generate_data.py
Script to generate random data for knapsack problem. It accepts **6** parameters.\
`python generate_data.py [items_number] [knapsack_capacity] [items_type] [max_weight] [max_cost] [file_name]`
* `items_number` —  integer value. Number of items for problem
* `knapsack_capacity` —  float value. Maximal weight that knapsack can contain
* `max_weight` —  float value. Maximal weight that can be among items. weight ∈ [1, max_weight]
* `max_cost` —  float value. Maximal cost than can be amont items. cost ∈ [2, max_cost)
* `file_name` —  str value. File name to write generated data.
### knapsack_dp.py
Dynamic algorithm to solve **Knapsack problem**. Can solve problem only with integer weights and costs. It accepts **1** paratemer.\
`python knapsack_dp.py [file_name]`
* `file_name` —  str value. File name with input data.
### knapsack_genetic.py
Python script to solve **Knapsack problem** using genetic algorithm. The algorithm does not guarantee an exact solution, it's heuristic.\
It accepts **2** parameters.\
` python knapsack_genetic.py [file_name] [iterations_number]`
* `file_name` —  str value. File name with input data.
* `iterations_number` —  int value. Number of iterations in genetic algorithm
## Contributors
Vadym Kinchur, vvkin
