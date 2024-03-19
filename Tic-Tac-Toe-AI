#Implementing the game of tic tac toe using the minmax algorithm 
import math
import time

class TicTacToe():
    def __init__(self):
        self.board = self.create_board()
        self.current_winner = None

    @staticmethod
    def create_board():
        return [' ' for _ in range(9)]

    def display_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def display_board_numbers():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.display_board_numbers()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' moves to square {}'.format(square))
                game.display_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Choose a position from 0-8: ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class AIPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if game.num_empty_squares() == 9:
            return 4  # AI starts from position 4
        else:
            return self.minimax(game, self.letter)['position']

    def minimax(self, state, player, alpha=-math.inf, beta=math.inf):
        max_player = 'X'
        other_player = 'O'

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                    state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
            for possible_move in state.available_moves():
                state.make_move(possible_move, player)
                sim_score = self.minimax(state, other_player, alpha, beta)
                state.board[possible_move] = ' '
                state.current_winner = None
                sim_score['position'] = possible_move
                if sim_score['score'] > best['score']:
                    best = sim_score
                alpha = max(alpha, best['score'])
                if alpha >= beta:
                    break
        else:
            best = {'position': None, 'score': math.inf}
            for possible_move in state.available_moves():
                state.make_move(possible_move, player)
                sim_score = self.minimax(state, other_player, alpha, beta)
                state.board[possible_move] = ' '
                state.current_winner = None
                sim_score['position'] = possible_move
                if sim_score['score'] < best['score']:
                    best = sim_score
                beta = min(beta, best['score'])
                if beta <= alpha:
                    break
        return best


if __name__ == '__main__':
    x_player = AIPlayer('X')
    o_player = HumanPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)
