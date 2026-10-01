class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
            
        digit_to_char = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        letters = []

        def backtrack(i):

            if i == len(digits):
                res.append(''.join(letters))
                return

            for char in digit_to_char[digits[i]]:
                letters.append(char)
                backtrack(i+1)
                letters.pop()

            return

        backtrack(0)
        return res

            

        
        