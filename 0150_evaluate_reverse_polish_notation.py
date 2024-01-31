import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        eval_stack = []
        operations ={"+": lambda a,b: a+b,
                     "-": lambda a,b: a-b,
                     "*": lambda a,b: a*b,
                     "/": lambda a,b: math.floor(a/b) if a/b > 0 else math.ceil(a/b)}
        
        for token in tokens:
            #when an operator is added
            if token in operations:
                
                second = int(eval_stack.pop())
                first = int(eval_stack.pop())
                
                #apply the operation
                result = operations[token](first,second)
                
                #return result to the stack
                eval_stack.append(result)
            else:
                
                #add element to the stack
                eval_stack.append(int(token))
        
        return eval_stack[-1]
