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
    
                box = i // 3 + (3 * (j//3))
                
                if num in box_dict[box] or num in col_dict[j] or num in row_dict[i]:
                    print(f"{i}, {j}")
                    print(num)
                    return False

                row_dict[i].add(num)
                col_dict[j].add(num)
                box_dict[box].add(num)

        return True



