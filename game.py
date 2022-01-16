from board import Board

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