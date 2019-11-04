#!/usr/bin/env python3
import operator
import numpy as np
import logging

# Uncomment for debugging print statements
#logging.basicConfig(level=logging.DEBUG)

OPS = {
    '+': operator.add, 
    '-': operator.sub,
    '/': operator.floordiv, 
    '*': operator.mul, 
    '^': operator.pow,
    '@': np.dot # NOTE: currently only works for 1D arrays
}

def split_args(myarg):
    """Split the operands and operations into a list
    
       myargs: str (non-empty)
    """
    pass

def calculate(arg):
    items = arg.split()
    stack = []
    for item in items:
        try:
            value = int(item)
            stack.append(value)
        except ValueError:
            # Assume that if the item is not an int or func, it is a list
            if item not in OPS:
                matrix = eval(item)
                stack.append(np.array(matrix))
            else:
                function = OPS[item]
                if len(stack) < 2:
                    raise TypeError('Malformed input')
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(function(num2, num1))
        logging.debug(stack)
    if len(stack) != 1:
        raise TypeError('Malformed input')
    return stack.pop()


def main():
    while True:
        result = calculate(input("rpn calc>"))
        print(result)

if __name__ == '__main__':
    main()
