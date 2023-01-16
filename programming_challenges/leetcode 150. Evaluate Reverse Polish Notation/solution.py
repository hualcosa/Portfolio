class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b,
        }
        
        stack = []
        for token in tokens:
            if token in operations:
                number2 = stack.pop()
                number1 = stack.pop()
                operation = operations[token]
                stack.append(operation(number1, number2))
            else:
                stack.append(int(token))
        return stack.pop()