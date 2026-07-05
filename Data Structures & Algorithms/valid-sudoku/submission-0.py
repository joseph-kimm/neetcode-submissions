class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = [set() for _ in range(9)]
        col_dict = [set() for _ in range(9)]
        box_dict = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                num = board[i][j]

                if num == ".":
                    continue

                if i < 3:
                    r = 0
                elif i < 6:
                    r = 1
                else: 
                    r = 2

                if j < 3:
                    c = 0
                elif j < 6:
                    c = 3
                else:
                    c = 6

                box = r + c

                if num in box_dict[box] or num in col_dict[j] or num in row_dict[i]:
                    print(f"{i}, {j}")
                    print(num)
                    return False

                row_dict[i].add(num)
                col_dict[j].add(num)
                box_dict[box].add(num)

        return True



