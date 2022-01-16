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

    def is_full(self) -> bool:
        for c in range(self.cols):
            if self.is_cell_open(0, c):
                return False
        return True

    def fill_cell(self, col: int, piece: str) -> tuple[int]:
        for r in range(self.rows - 1, -1, -1):
            if self.is_cell_open(r, col):
                self.board[r][col] = piece
                return r, col