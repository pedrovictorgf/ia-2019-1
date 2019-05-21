import random


# A class to represent our board state
class Board:
    def __init__(self, n):
        self.n = n  # The size of the problem
        self.board = n * [0]  # Just initializing a board with size n and no queens placed on it
        self.count = 0  # Number of queens already placed at the board

    # A method to return a copy of the board state
    def copy(self):
        copy = Board(self.n)
        copy.board = self.board.copy()
        return copy


# A method that tests if the board has reached a goal state, that is, have n queens placed on it and no attacks
# between them
def is_goal(board):
    if board.count == board.n and calc_number_of_attacks(board) == 0:
        return True
    else:
        return False


# A method for calculating the number of attacks in the board, it already returns the total number of attacks divided
# by two since we only count the attack between queen A and queen b once.
def calc_number_of_attacks(board):
    number_of_attacks = 0
    for i in range(board.count):
        for j in range(i + 1, board.count):
            if board.board[i] == board.board[j] or board.board[j] + abs(i - j) == board.board[i] or board.board[
                j] - abs(i - j) == \
                    board.board[i]:
                number_of_attacks += 1
    return number_of_attacks


# A method for inserting a new board state in a priority queue, but if the state is in the tabu list it'll be the last
# element of the queue
def insert_priority_queue(queue, element, tabu_list):
    size = len(queue)
    if size > 0:
        for i in range(size):
            if calc_number_of_attacks(element) < calc_number_of_attacks(queue[i]) and element not in tabu_list:
                return queue[:i] + [element] + queue[i:]
            elif i == size - 1:
                return queue + [element]
    else:
        return [element]


# A method for generating a random initial state
def generate_random_initial_state(n):
    board = Board(n)
    board.count = n
    for i in range(board.n):
        board.board[i] = random.randint(1, board.n)

    return board


# A method for generating all the possible states from the current state that aren't in the tabu list
def generate_possible_states(board, tabu_list):
    new_board_states = []
    for i in range(board.n):
        queen_position = board.board[i]
        possible_positions = range(1, board.n + 1)
        possible_positions = [position for position in possible_positions if position != queen_position]
        for new_position in possible_positions:
            new_board_state = Board(board.n)
            new_board_state.count = board.n
            new_board_state.board = board.board.copy()
            new_board_state.board[i] = new_position
            new_board_states = insert_priority_queue(new_board_states, new_board_state, tabu_list)

    return new_board_states


# A method for the update of the tabu list, wich keeps track of the last two moves that we made
def update_tabu_list(tabu_list, new_tabu_state):
    if len(tabu_list) < 2:
        tabu_list.append(new_tabu_state)
    else:
        tabu_list[0] = tabu_list[1]
        tabu_list[1] = new_tabu_state

    return tabu_list


def local_search(board):
    current_board = board  # This is the queue of paths to be explored in this graph
    tabu_list = []
    same_value = 0
    while True:  # When the queue is empty it means we looked all the possible paths
        if same_value > 10:
            return current_board
        best_neighbour = generate_possible_states(current_board, tabu_list)[0]
        tabu_list = update_tabu_list(tabu_list, best_neighbour)
        if calc_number_of_attacks(current_board) < calc_number_of_attacks(best_neighbour):
            return current_board
        else:
            if calc_number_of_attacks(current_board) == calc_number_of_attacks(best_neighbour):
                same_value += 1
            current_board = best_neighbour


# You can just input the n size for the n-queen problem
N = 8
b = generate_random_initial_state(N)
solution = local_search(b)
print(solution.board, calc_number_of_attacks(solution))
