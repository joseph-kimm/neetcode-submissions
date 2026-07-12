class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {'{':'}','[':']','(':')'}
        stack = []

        for b in s:

            if b in brackets.keys():
                stack.append(b)

            else:
                if len(stack) == 0 or brackets[stack[-1]] != b:
                    return False

                stack.pop()

        if len(stack) == 0:
            return True

        else:
            return False
        