class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {'+', '-', '*', '/'}
        stack = []
        
        for c in tokens:

            if c in operators:

                num2 = stack.pop()
                num1 = stack.pop()

                if c == '+':
                    stack.append(num1 + num2)

                elif c == '-':
                    stack.append(num1 - num2)

                elif c == '*':
                    stack.append(num1 * num2)

                else:
                    stack.append(int(num1 / num2))

            else:
                stack.append(int(c))

        return stack[0]