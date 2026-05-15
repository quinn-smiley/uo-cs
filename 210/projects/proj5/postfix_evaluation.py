def is_operand(operand):
    try: 
        float(operand)
    except (ValueError, TypeError): 
        return False
    else: 
        return True
    
# print(is_operand("3"))
# print(is_operand("3.5"))
# print(is_operand("a"))

def is_operator(operator):
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        return True
    else: 
        return False
    
# print(is_operator("3"))
# print(is_operator("+"))
# print(is_operator("!"))

def apply_operator(op, oper_1, oper_2):
    if op == "+":
        return oper_1 + oper_2
    elif op == "-":
        return oper_1 - oper_2
    elif op == "*":
        return oper_1 * oper_2
    elif op == "/":
        return oper_1 / oper_2
    else: 
        print("Invalid operator")

# print(apply_operator("*", 3, 4))
# print(apply_operator("/", 4, 2))

def eval_postfix(expr_str):
    chars = expr_str.split()
    stack = []
    for char in chars:
        if is_operand(char) == True:
            stack.append(float(char))
        elif is_operator(char) == True:
            b = stack.pop()
            a = stack.pop()
            result = apply_operator(char, a, b)
            stack.append(result)
    
    if len(stack) != 1:
        return "error on postfix expression"
            
    return stack

# print(eval_postfix("3 4 +"))
# print(eval_postfix("3 4 + 7 *"))
# print(eval_postfix("3 3.5 4 + 7 * /"))
# print(eval_postfix("3 3.5 4 +"))
