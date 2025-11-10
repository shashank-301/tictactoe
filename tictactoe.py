class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current = 'X'

    def print_board(self):
        for i in range(3):
            print('|'.join(self.board[i * 3:(i + 1) * 3]))
            if i < 2:
                print('-----')

    def make_move(self, pos):
        if self.board[pos] == ' ':
            self.board[pos] = self.current
            return True
        return False

    def switch(self):
        self.current = 'O' if self.current == 'X' else 'X'

    def winner(self):
        b = self.board
        for i in range(3):
            if b[3 * i] == b[3 * i + 1] == b[3 * i + 2] != ' ':
                return b[3 * i]
            if b[i] == b[i + 3] == b[i + 6] != ' ':
                return b[i]
        if b[0] == b[4] == b[8] != ' ':
            return b[0]
        if b[2] == b[4] == b[6] != ' ':
            return b[2]
        if ' ' not in b:
            return 'Draw'
        return None

    def reset(self):
        self.board = [' '] * 9
        self.current = 'X'

if __name__ == "__main__":
    game = TicTacToe()
    while not game.winner():
        game.print_board()
        try:
            pos = int(input(f"Player {game.current} move (0-8): "))
            if not (0 <= pos < 9):
                print("Invalid position.")
                continue
            if not game.make_move(pos):
                print("Position taken.")
                continue
            if game.winner():
                game.print_board()
                print("Game Over! Winner:", game.winner())
                break
            game.switch()
        except ValueError:
            print("Please enter a valid number (0-8).")
