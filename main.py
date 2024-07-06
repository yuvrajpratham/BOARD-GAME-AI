import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print('|'.join(self.board[i:i+3]))

    def is_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_board_full()

    def make_move(self, position):
        if 0 <= position < 9 and self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0 or board.is_game_over():
        if board.is_winner('X'):
            return -1
        elif board.is_winner('O'):
            return 1
        else:
            return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board.board[i] == ' ':
                board.board[i] = 'O'
                eval = minimax(board, depth - 1, False, alpha, beta)
                board.board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board.board[i] == ' ':
                board.board[i] = 'X'
                eval = minimax(board, depth - 1, True, alpha, beta)
                board.board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board):
    best_move = -1
    best_eval = -math.inf

    for i in range(9):
        if board.board[i] == ' ':
            board.board[i] = 'O'
            move_eval = minimax(board, 4, False, -math.inf, math.inf)
            board.board[i] = ' '

            if move_eval > best_eval:
                best_eval = move_eval
                best_move = i

    return best_move

def main():
    game = TicTacToe()

    while not game.is_game_over():
        game.print_board()

        if game.current_player == 'X':
            position = int(input("Enter your move (0-8): "))
            if not game.make_move(position):
                print("Invalid move. Try again.")
        else:
            print("AI is thinking...")
            ai_move = find_best_move(game)
            game.make_move(ai_move)

    game.print_board()

    if game.is_winner('X'):
        print("You win!")
    elif game.is_winner('O'):
        print("AI wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()

