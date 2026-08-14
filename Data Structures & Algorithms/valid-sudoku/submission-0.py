from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cellVal = board[r][c]
                if cellVal == ".":
                    continue
                
                if (cellVal in rows[r] or
                    cellVal in cols[c] or
                    cellVal in squares[(r//3,c//3)]):
                    return False
                
                rows[r].add(cellVal)
                cols[c].add(cellVal)
                squares[(r//3,c//3)].add(cellVal)

        return True