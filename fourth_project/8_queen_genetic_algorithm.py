import random

NUMBER_OF_GENERATIONS = 1000  # Since there was no specification for the generations limit i've set it to 1000
POPULATION_SIZE = 5  # The size of the population
MUTATION_RATE = 1  # The rate of a child suffer a mutation, expressed from 0 to 10
CROSS_OVER_POINT = 3
N = 8  # The size of the n-queen problem


# A method for calculating the number of nonattacking pair of queens in the board, this method will be our fitness
# function, for the 8-queen problem the solution fitness will be 28
def fitness_function(board):
    total_non_attacking_pair_of_queens = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or board[j] + abs(i - j) == board[i] or board[j] - abs(i - j) == board[i]:
                pass
            else:
                total_non_attacking_pair_of_queens += 1

    return total_non_attacking_pair_of_queens


# A method for inserting a new board state in a priority queue, in which the priority is the higher the fitness
# function the better
def insert_priority_queue(queue, element):
    size = len(queue)
    if size > 0:
        for i in range(size):
            if element[1] > queue[i][1]:
                return queue[:i] + [element] + queue[i:]
            elif i == size - 1:
                return queue + [element]
    else:
        return [element]


# A method that generate a random population with size POPULATION_SIZE
def generate_random_initial_population():
    random_initial_population = []
    for i in range(POPULATION_SIZE):
        board_state = []
        for j in range(N):
            board_state.append(random.randint(1, N))
        individual = (board_state, fitness_function(board_state))
        random_initial_population = insert_priority_queue(random_initial_population, individual)
    return random_initial_population


# Get a random parent based on each individual fitness function
def get_parent(population):
    total_fitness_sum = 0
    for individual in population:
        total_fitness_sum += individual[1]

    rand_int = random.randint(1, total_fitness_sum)
    aux = population[0][1]
    for individual in population:
        if rand_int <= aux:
            return individual
        else:
            aux += individual[1]


# Reproduces the two parents
def reproduce(first_parent, second_parent):
    return first_parent[0][:CROSS_OVER_POINT] + second_parent[0][CROSS_OVER_POINT:]


# Mutates one attribute of the individual at a random position
def mutate_individual(individual):
    random_position = random.randint(0, N - 1)
    mutation = random.randint(1, N)
    individual[random_position] = mutation
    return individual


# Checks if the individual is a goal state
def is_goal_state(individual):
    if individual[1] == 28:
        return True
    else:
        return False


def genetic_algorithm(population):
    for i in range(NUMBER_OF_GENERATIONS):
        new_population = [population[0]]
        for j in range(POPULATION_SIZE - 1):
            first_parent = get_parent(population)
            second_parent = get_parent(population)
            child = reproduce(first_parent, second_parent)

            will_suffer_mutation = random.randint(1, 10)
            if will_suffer_mutation <= MUTATION_RATE:
                child = mutate_individual(child)

            child = (child, fitness_function(child))
            if is_goal_state(child):
                return child, i

            new_population = insert_priority_queue(new_population, child)

        population = new_population
    return population[0]


initial_population = generate_random_initial_population()
print(genetic_algorithm(initial_population))
