class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token in '+-*/':
                b, a = stk.pop(), stk.pop() 
                
                if token == '+':
                    stk.append(a+b)
                elif token == '-':
                    stk.append(a-b)
                elif token == '*':
                    stk.append(a*b)
                else:
                    division = a / b
                    if division < 0:
                        stk.append(ceil(division))
                    else:
                        stk.append(int(division))
            else:
                stk.append(int(token))
        
        return stk[0]