# Time Complexity: O(N)
# Space Complexity: O(N) when stack is full
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "-", "*", "/"])
        stack = []
        for token in tokens:
            if token in operators:
                num2, num1 = stack.pop(), stack.pop()
                result = 0
                if token == "+": result = num1 + num2
                elif token == "-": result = num1 - num2
                elif token == "*": result = num1 * num2
                elif token == "/": result = int(num1 / num2)
                stack.append(result)
            elif len(tokens) < 2: # if the stack is only 1 in length
                # Can't append nor operate, so return the token as is
                return int(token)
            else:
                stack.append(int(token))
        return stack[-1]
