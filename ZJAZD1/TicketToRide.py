from easyAI import TwoPlayerGame
from easyAI.Player import Human_Player


class TicTacToe(TwoPlayerGame):
    """The board positions are numbered as follows:
     1  2   3   4   5   6   7
     8  9  10  11  12  13  14
     15 16 17  18  19  20  21
     22 23 24  25  26  27  28
     29 30 31  32  33  34  35
    """

    def __init__(self, players):
        self.rows = 5
        self.columns = 7
        self.points_score_board = [0, 0]
        self.last_move_position = 0
        self.players = players
        self.board = [0 for i in range(self.rows * self.columns)]
        self.current_player = 1  # player 1 starts.

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.current_player
        self.last_move_position = int(move) - 1

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move) - 1] = 0

    def lose(self):
        return self.points_score_board[self.opponent_index - 1] >= 2

    def is_over(self):
        return (self.possible_moves() == []) or self.lose()

    def show(self):
        print(
            "\n"
            + "\n".join(
                [
                    " ".join([[".", "O", "X"][self.board[self.columns * j + i]] for i in range(self.columns)])
                    for j in range(self.rows)
                ]
            )
        )

    def is_position_valid(self, i):
        if i >= (self.rows * self.columns):
            return False
        if i < 0:
            return False
        return True

    def are_positions_in_row(self, pos1, pos2, pos3):
        row_number = pos1 % self.columns
        return row_number == pos2 % self.columns and row_number == pos3 % self.columns

    def make_three(self, pos1, pos2, pos3):

        if self.is_position_valid(self, pos1) and self.is_position_valid(self, pos2) and self.is_position_valid(self,
                                                                                                                pos3):
            symbol = self.board[pos1]
            return symbol == self.board[pos2] and symbol == self.board[pos3]
        else:
            return False

    def last_score(self):
        if self.make_three(self, self.last_move_position, self.last_move_position - self.columns,
                           self.last_move_position - 2 * self.columns) \
                or self.make_three(self, self.last_move_position, (self.last_move_position + self.columns),
                                   (self.last_move_position + (2 * self.columns))) \
                or self.make_three(self, self.last_move_position, (self.last_move_position - self.columns),
                                   (self.last_move_position + self.columns)) \
                or (self.make_three(self, self.last_move_position, (self.last_move_position - 1),
                                    (self.last_move_position - 2)) and self.are_positions_in_row(self,
                                                                                                 self.last_move_position,
                                                                                                 self.last_move_position - 1,
                                                                                                 self.last_move_position - 2)) \
                or (self.make_three(self, self.last_move_position, (self.last_move_position + 1),
                                    (self.last_move_position + 2)) and self.are_positions_in_row(self,
                                                                                                 self.last_move_position,
                                                                                                 self.last_move_position + 1,
                                                                                                 self.last_move_position + 2)) \
                or (self.make_three(self, self.last_move_position, (self.last_move_position - 1),
                                    (self.last_move_position + 1)) and self.are_positions_in_row(self,
                                                                                                 self.last_move_position,
                                                                                                 self.last_move_position - 1,
                                                                                                 self.last_move_position + 1)) \
                or self.make_three(self, self.last_move_position, (self.last_move_position - self.columns - 1),
                                   (self.last_move_position - (2 * self.columns + 1))) \
                or self.make_three(self, self.last_move_position, (self.last_move_position + self.columns + 1),
                                   (self.last_move_position + (2 * self.columns + 1))) \
                or self.make_three(self, self.last_move_position, (self.last_move_position - self.columns - 1),
                                   (self.last_move_position + self.columns + 1)) \
                or self.make_three(self, self.last_move_position, (self.last_move_position - self.columns + 1),
                                   (self.last_move_position - (2 * self.columns - 1))) \
                or self.make_three(self, self.last_move_position, (self.last_move_position + self.columns - 1),
                                   (self.last_move_position + (2 * self.columns - 1))) \
                or self.make_three(self, self.last_move_position, (self.last_move_position - self.columns + 1),
                                   (self.last_move_position + self.columns - 1)):
            return -5
        return 0

    def scoring(self):
        return -100 if self.lose() else self.last_score()


if __name__ == "__main__":
    from easyAI import AI_Player, Negamax

    ai_algo = Negamax(6)
    TicTacToe([Human_Player(), AI_Player(ai_algo)]).play()
