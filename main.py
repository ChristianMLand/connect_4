class Board:
    def __init__(self, cols: int = 7, rows: int = 6):
        self.cols = cols
        self.rows = rows
        self.board = [['_' for _ in range(cols)] for _ in range(rows)]

    def display(self) -> None:
        for row in self.board:
            print(row)

    def is_valid_col(self, col: str) -> bool:
        if col.isnumeric():
            col = int(col)
            return 0 <= col < self.cols and self.is_cell_open(0, col)
        return False

    def is_cell_in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_cell_open(self, row: int, col: int) -> bool:
        return self.board[row][col] == '_'

    def count_in_direction(self, row: int, col: int, rise: int, run: int) -> int:
        off = 0
        y, x = row, col
        while self.is_cell_in_bounds(y, x) and self.board[y][x] == self.board[row][col]:
            off += 1
            y, x = row + off * rise, col + off * run
        return off

    def is_board_full(self) -> bool:
        for c in range(self.cols):
            if self.is_cell_open(0, c):
                return False
        return True

    def fill_cell(self, col: int, piece: str) -> tuple[int]:
        for r in range(self.rows - 1, -1, -1):
            if self.is_cell_open(r, col):
                self.board[r][col] = piece
                return r, col

class Game:
    def __init__(self, goal: int = 4):
        self.goal = goal
        self.reset()

    def reset(self) -> None:
        self.board = Board()
        self.game_over = False
        self.turn = 0

    @property
    def current_turn(self):
        return 'X' if self.turn % 2 else 'O'

    def get_move(self) -> int:
        print(f"Player {self.current_turn}'s turn")
        while not self.board.is_valid_col(move := input(f"Pick move (0-{self.board.cols-1}): ").strip()) :
            print("Please choose a valid move!")
        return int(move)

    def is_win_move(self, row: int, col: int) -> bool:
        dirs = [
            self.board.count_in_direction(row, col, 0, 1) + self.board.count_in_direction(row, col, 0, -1) - 1,
            self.board.count_in_direction(row, col, 1, 1) + self.board.count_in_direction(row, col, -1, -1) - 1,
            self.board.count_in_direction(row, col, 1, -1) + self.board.count_in_direction(row, col, -1, 1) - 1,
            self.board.count_in_direction(row, col, 1, 0)
        ]
        for dir in dirs:
            if dir >= self.goal:
                return True
        return False

    def is_game_over(self, row: int, col: int) -> bool:
        win = self.is_win_move(row, col)
        tie = self.board.is_board_full()
        if win or tie:
            self.board.display()
            print(f"Game over: {f'Player {self.current_turn} wins' if win else 'Tie'}!")
            return True
        return False

    def play(self) -> None:
        while not self.game_over:
            self.board.display()
            row,col = self.board.fill_cell(self.get_move(), self.current_turn)
            self.game_over = self.is_game_over(row, col)
            self.turn += 1

if __name__ == "__main__":
    game = Game()
    game.play()