class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for char in tokens:
            if char in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                res_exp = str(num1) + char + str(num2)
                print(res_exp)
                stack.append(int(eval(res_exp)))
            else:
                stack.append(char)
        return(stack[0])
                
            
        