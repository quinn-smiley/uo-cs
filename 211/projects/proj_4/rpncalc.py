"""Reverse Polish Notation calculator.

"""

from expr import *
from typing import List, Type

def is_binop(op:str)->bool:
    return op in {"+", "-", "*", "//"}

def is_unop(op:str)->bool:
    return op in {"@", "~"}

def is_var(op:str)->bool:
    return op not in {"+", "-", "*", "//", "@", "~", "="}

def binop_class(op: str) -> Type[BinOp]:
    if op == "+":
        return Plus
    elif op == "-":
        return Minus
    elif op == "*":
        return Times
    elif op == "//":
        return Div
    else:
        raise ValueError(f"Unknown binary operator: {op}")
    
def unop_class(op: str) -> Type[UnOp]:
    if op == "@":
        return Abs
    elif op == "~":
        return Neg
    else: 
        raise ValueError(f"Unknown unary operator: {op}")

def rpn_parse(text: str) -> List[Expr]:
    """Parse text in reverse Polish notation
    into a list of expressions (exactly one if
    the expression is balanced).
    Example:
        rpn_parse("5 3 + 4 *")
          => [ Times(Plus(IntConst(5), IntConst(3)), IntConst(4))))]
    """
    tokens = text.split()
    stack = []

    for tok in tokens: 
        try: 
            n = int(tok)
            stack.append(Const(n))
            continue
        except ValueError: 
            pass


        if is_binop(tok): # Asked Cursor the best way to go about structuring this
            if len(stack) < 2: 
                raise ValueError(f"Not enough operands for a binary operator")
            
            right = stack.pop()
            left = stack.pop()

            binop_cls = binop_class(tok)
            new_expr = binop_cls(left, right)

            stack.append(new_expr)
        
        elif is_unop(tok):
            if len(stack) < 1: 
                raise ValueError(f"Not enough operands for a unary operator")
            
            left = stack.pop()

            unop_cls = unop_class(tok)
            new_expr = unop_cls(left)

            stack.append(new_expr)
        
        elif tok == "=":
            if len(stack) < 2: 
                raise ValueError("Not enough operands for assignment '='")
            
            right = stack.pop()
            left = stack.pop()

            new_expr = Assign(right, left)
            stack.append(new_expr)

        elif is_var(tok):
            stack.append(Var(tok))
        
        else: 
            raise ValueError("Invalid input")

    return stack

def calc(text: str):
    """Read and evaluate a single line formula."""
    exprs = rpn_parse(text)
    expr = exprs[0]
    result = expr.eval()
    return result

def rpn_calc(): # Asked Cusor how to correctly format the input based on the instructions
    while True: 
        text = input("Expression (return to quit):")
        if text.strip() == "":
            return
        
        exprs = rpn_parse(text)
        expr = exprs[0]

        result = expr.eval()
        print(f"({expr}) => {result}")



if __name__ == "__main__":
    """RPN Calculator as main program"""
    rpn_calc()
