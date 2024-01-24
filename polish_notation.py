import math

def infix_to_postfix(infix_expression):
    postfix = ""
    calc_stack = []

    number = ""

    for c in infix_expression:
        if c.isdigit():
            number += c
        else:
            if number:
                postfix += f"{number} "
                number = ""

            if c == '(':
                calc_stack.append(c)
            elif c == ')':
                while calc_stack and calc_stack[-1] != '(':
                    postfix += f"{calc_stack.pop()} "
                calc_stack.pop()
            elif is_operation(c):
                while calc_stack and is_operation(calc_stack[-1]) and procedure(calc_stack[-1]) >= procedure(c):
                    postfix += f"{calc_stack.pop()} "
                calc_stack.append(c)
            elif c == '!':
                postfix += "! "
            elif c != ' ':
                raise ValueError("Invalid expression")

    if number:
        postfix += f"{number} "

    postfix += " ".join(calc_stack[::-1]) + " "

    return postfix


def is_operation(c):
    return c in {'+', '-', '*', '/', '^', '%', 'l', 'c', 's', 't', 'g', '_', '!'}


def procedure(op):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'l': 4, 'c': 4, 's': 4, 't': 4, 'g': 4, '_': 5, '!': 5}
    return precedence.get(op, 0)


def factorial(n):
    return 1 if n in {0, 1} else n * factorial(n - 1)


operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else ValueError("Division by zero"),
    '^': lambda x, y: x ** y,
    '%': lambda x, y: x % y if y != 0 else ValueError("Modul by zero"),
    'l': lambda x: math.log(x) if x > 0 else ValueError("Non-positive number in log"),
    'c': lambda x: math.cos(x),
    's': lambda x: math.sin(x),
    't': lambda x: math.tan(x),
    'g': lambda x: 1 / math.tan(x),
    '_': lambda x: -x,
    '!': lambda x: factorial(x) if x >= 0 else ValueError("Factorial of a negative number"),
}


def perform_operation(op, operand1, operand2=0):
    if op in operations:
        if operand2 == 0:
            return operations[op](operand1)
        return operations[op](operand1, operand2)
    else:
        raise ValueError("Invalid operator")


def evaluate_expression(expression):
    operand_stack = []
    number = ""

    for c in expression:
        if c.isdigit():
            number += c
        elif c == ' ' and number:
            operand_stack.append(int(number))
            number = ""
        elif is_operation(c):
            if c in {'l', 'c', 's', 't', 'g', '_', '!'}:
                operand = operand_stack.pop()
                result = perform_operation(c, operand)
                operand_stack.append(result)
            else:
                if len(operand_stack) < 2:
                    raise ValueError("Invalid expression")
                operand2, operand1 = operand_stack.pop(), operand_stack.pop()
                result = perform_operation(c, operand1, operand2)
                operand_stack.append(result)

    if number:
        operand_stack.append(int(number))

    if len(operand_stack) != 1:
        raise ValueError("Invalid expression")

    return operand_stack[0]

infix_expression = "4+_21+2!"
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix Expression:", postfix_expression)
print("Result:", evaluate_expression(postfix_expression))