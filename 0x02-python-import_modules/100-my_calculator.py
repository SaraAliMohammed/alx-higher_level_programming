#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    count = len(sys.argv) - 1
    if(count != 3):
        print("Usage: ./{} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    operators = ['+', '-', '*', '/']
    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    result = 0
    if operator == '+':
        result = calculator_1.add(a, b)
    elif operator == '-':
        result = calculator_1.sub(a, b)
    elif operator == '*':
        result = calculator_1.mul(a, b)
    else:
        result = calculator_1.div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
