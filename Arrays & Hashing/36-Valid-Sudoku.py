class Solution(object):
    def isValidSudoku(self, board):
        # Testar se há repetições em 3x3
        for j in range(0,9,3):
            for k in (0,9,3):
                test = set()
                for x in range(3):
                    for y in range(3):
                        if board[j+x][k+y] in test and board[j+x][k+y] != '.':
                            return False
                        test.add(board[j+x][k+y])

        # Testar se há repetições em linhas
        for l in board:
            test = set()
            for i in range(9):
                if l[i] in test and l[i] != '.':
                    return False
                test.add(l[i])

        # Testar se há repetições em colunas
        for j in range(9):
            test = set()
            for i in range(9):
                if board[i][j] in test and board[i][j] != '.':
                    return False
                test.add(board[i][j])
        return True
