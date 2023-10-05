#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if(count != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = ['+', '-', '*', '/']
    operator = sys.argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = 0
    from calculator_1 import add, sub, mul, div
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    else:
        result = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
