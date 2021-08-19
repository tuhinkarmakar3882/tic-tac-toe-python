class Board:
    def __init__(self, size):
        self._board = []
        self._rows = size
        self._cols = size
        self._create_board()

    def display(self):
        for row in range(self._rows):
            for col in range(self._cols):
                self._pretty_print(col, row)
            print()
        print()

    def show_options(self):
        print("Select a cell to put a marker:")
        cell_number = 0

        for row in range(self._rows):
            for col in range(self._cols):
                if self._board[row][col] is None:
                    print(cell_number, end=" ")
                else:
                    print('.', end=" ")

                cell_number += 1
            print()
        print()

    def place_marker(self, cell_number, marker):
        col_num, row_num = self._extract_row_and_column_from(cell_number)

        self._board[row_num][col_num] = marker

    def is_valid(self, cell_number):
        try:
            cell_number = int(cell_number)
            grid_pos = 0

            for row in range(self._rows):
                for col in range(self._cols):
                    if cell_number == grid_pos and self._board[row][col] is None:
                        return True
                    grid_pos += 1

            return False
        except ValueError:
            return False

    def has_consecutive_marker_on_columns(self):
        for col in range(self._cols):
            has_match = True
            prev_marker = self._board[0][col]

            if prev_marker is None:
                continue

            for row in range(self._rows):
                current_cell_marker = self._board[row][col]
                if current_cell_marker != prev_marker or current_cell_marker is None:
                    has_match = False
                    break

            if has_match:
                return True

        return False

    def has_consecutive_marker_on_rows(self):
        for row in range(self._cols):
            has_match = True
            prev_marker = self._board[row][0]

            if prev_marker is None:
                continue

            for col in range(self._rows):
                current_cell_marker = self._board[row][col]
                if current_cell_marker != prev_marker or current_cell_marker is None:
                    has_match = False
                    break

            if has_match:
                return True

        return False

    def has_consecutive_marker_on_diagonal(self):
        return self._has_match_in_first_diagonal() or self._has_match_in_second_diagonal()

    def is_full(self):
        for row in range(self._rows):
            for col in range(self._cols):
                if self._board[row][col] is None:
                    return False
        return True

    def _extract_row_and_column_from(self, cell_number):
        row_num, col_num = None, None
        grid_pos = 0
        for row in range(self._rows):
            for col in range(self._cols):
                if cell_number == grid_pos:
                    row_num = row
                    col_num = col
                grid_pos += 1
        return col_num, row_num

    def _create_board(self):
        for row in range(self._rows):
            temp = []
            for col in range(self._cols):
                temp.append(None)

            self._board.append(temp)

    def _pretty_print(self, col, row):
        if self._board[row][col] is None:
            print('-', end=" ")
        else:
            print(self._board[row][col], end=" ")

    def _has_match_in_first_diagonal(self):
        has_match = True
        prev_marker = self._board[0][0]
        for i in range(self._rows):
            current_cell_marker = self._board[i][i]
            if current_cell_marker != prev_marker or current_cell_marker is None:
                has_match = False
                break

        return has_match

    def _has_match_in_second_diagonal(self):
        last_row = self._rows - 1
        last_column = self._cols - 1
        prev_marker = self._board[last_row][last_column]
        has_match = True

        for i in range(last_row, -1, -1):
            current_cell_marker = self._board[i][i]
            if current_cell_marker != prev_marker or current_cell_marker is None:
                has_match = False
                break

        return has_match
