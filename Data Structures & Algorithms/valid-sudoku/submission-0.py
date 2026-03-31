class Solution:
    def getIndFromRowAndCol(self, row, col) -> int:
        return 18 + (row // 3) * 3 + (col // 3)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        list_of_sets = [set() for _ in range(27)]
        n = len(board)
        m = len(board[0])

        for row in range(n):
            for col, val in enumerate(board[row]):
                if val == ".":
                    continue

                if val in list_of_sets[row]:
                    return False
                else:
                    list_of_sets[row].add(val)
                if val in list_of_sets[col + 9]:
                    return False
                else:
                    list_of_sets[col + 9].add(val)
                sub_box_ind = self.getIndFromRowAndCol(row, col)
                if val in list_of_sets[sub_box_ind]:
                    return False
                else:
                    list_of_sets[sub_box_ind].add(val)
        
        return True