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


# A method for inserting a new board state in a priority queue
def insert_priority_queue(queue, element):
    size = len(queue)
    if size > 0:
        for i in range(size):
            if calc_number_of_attacks(element) < calc_number_of_attacks(queue[i]):
                return queue[:i] + [element] + queue[i:]
            elif i == size - 1:
                return queue + [element]
    else:
        return [element]


def greedy_best_first_search(board):
    frontier_of_boards_queue = [board]  # This is the queue of paths to be explored in this graph

    if is_goal(board):  # If the initial board state is a goal state, then there
        # is no search to be done, we already have the solution
        return board

    while frontier_of_boards_queue:  # When the queue is empty it means we looked all the possible board states
        current_board = frontier_of_boards_queue.pop(0)  # Current board state we are analyzing

        if is_goal(current_board):
            return current_board
        elif current_board.count < current_board.n:  # If we weren't in a goal state, generate all possibilities from
            # the  current state
            for i in range(current_board.n):
                new_board = current_board.copy()
                new_board.board[current_board.count] = i + 1
                new_board.count = current_board.count + 1
                frontier_of_boards_queue = insert_priority_queue(frontier_of_boards_queue, new_board)

    return None


b = Board(6)
solution = greedy_best_first_search(b)
print(solution.board, calc_number_of_attacks(solution))
