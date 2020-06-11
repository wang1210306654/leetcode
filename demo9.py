from typing import List
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        a = ''.join(board).replace(" ", "")
        xn = a.count('X')
        on = a.count('O')
        if xn < on or xn - on > 1 or len(''.join(board)):
            return False
        if len(''.join(board)) == 9:
            return True
        if len(a) < 5:
            return False
        return self.check(board)

    def check(board):
        for i in range(3):
            if ''.join(board[i]).count('X') == 3 or ''.join(board[i]).count('O'):
                return True

