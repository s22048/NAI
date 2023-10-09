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
        self.players = players
        self.board = [0 for i in range(self.rows * self.columns)]
        self.current_player = 1  # player 1 starts.

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.current_player

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move) - 1] = 0

    def lose(self):
        return self.get_score_for_symbol(self.opponent_index) >= 5

    def get_score_for_symbol(self, symbol):
        score = 0
        for i in range(1, self.rows * self.columns) :
            if(self.is_in_center_of_score(i, symbol)) :
                score = score + 1
        return score

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

        print ("\n" + str(self.get_score_for_symbol(1)) + ":" + str(self.get_score_for_symbol(2)))

    def is_position_valid(self, i):
        if i >= (self.rows * self.columns):
            return False
        if i < 0:
            return False
        return True

    def are_positions_in_row(self, pos1, pos2, pos3):
        first_column_number = (pos1 - 1) // self.columns
        return first_column_number == (pos2 - 1) // self.columns and first_column_number == (pos3 - 1) // self.columns

    def make_three(self, pos1, pos2, pos3):
        if self.is_position_valid(pos1 - 1) and self.is_position_valid(pos2 - 1) and self.is_position_valid(pos3 - 1):
            symbol = self.board[pos1 - 1]
            temp = symbol == self.board[pos2 - 1] and symbol == self.board[pos3 - 1]
            return temp
        else:
            return False

    def isNotSideBorder(self, pos):
        return (pos - 1) % self.columns != 0 and (pos - 1) % self.columns != self.columns - 1

    def is_in_center_of_score(self, pos, symbol):
        if(self.board[pos - 1] != symbol):
            return False

        if self.make_three(pos, (pos - self.columns), (pos + self.columns)) \
                or (self.make_three(pos, (pos - 1), (pos + 1)) and self.are_positions_in_row(pos, pos - 1,pos + 1)) \
                or (self.isNotSideBorder(pos) and self.make_three(pos, (pos - self.columns - 1), (pos + self.columns + 1))) \
                or  (self.isNotSideBorder(pos) and self.make_three(pos, (pos - self.columns + 1), (pos + self.columns - 1))):
            return True

        return False

    def scoring(self):
        return -100 if self.lose() else 0


if __name__ == "__main__":
    from easyAI import AI_Player, Negamax

    ai_algo = Negamax(4)
    TicTacToe([Human_Player(), AI_Player(ai_algo)]).play()
