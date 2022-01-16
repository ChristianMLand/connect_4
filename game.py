from board import Board

class Game:
    def __init__(self, goal: int = 4):
        self.goal = goal
        self.reset()

    @property
    def current_piece(self):
        return 'O' if self.turn % 2 else 'X'

    @property
    def game_over(self) -> bool:
        return self.has_won() or self.board.is_full()

    def reset(self) -> None:
        self.board = Board()
        self.last_move = -1,-1
        self.turn = 0

    def get_move(self) -> int:
        move = ''
        while not self.is_valid_move(move):
            move = input(f"Pick move (0-{self.board.cols-1}): ").strip()
        return int(move)

    def is_valid_move(self, move: str) -> bool:
        if move.isnumeric():
            col = int(move)
            return self.board.is_cell_in_bounds(0,col) and self.board.is_cell_open(0, col)
        return False

    def has_won(self) -> bool:
        row, col = self.last_move
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

    def play(self) -> None:
        while not self.game_over:
            self.turn += 1
            self.board.display()
            print(f"Player {self.current_piece}'s turn")
            self.last_move = self.board.fill_cell(self.get_move(), self.current_piece)
        self.board.display()
        print(f'Player {self.current_piece} wins!' if self.has_won() else 'Tie!')