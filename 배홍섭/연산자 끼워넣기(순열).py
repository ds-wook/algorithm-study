N = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))

# N = 2
# numbers = [5,6]
# operations = [0,0,1,0]

# N = 3
# numbers = [3,4,5]
# operations = [1,0,1,0]

# N = 6
# numbers = [1,2,3,4,5,6]
# operations = [2,1,1,1]

import math
from itertools import permutations

ops = ["+", "-", "*", "/"]
candidates = []
for idx, operation in enumerate(operations):  # 최대 10개
    candidates.extend(ops[idx] * operation)
# print(op2num)
# print(candidates)

candidates = list(permutations(candidates))  # 최대 10! = 3,628,800번..
# print(math.factorial(10))
# print(candidates)

max_value, min_value = int(-1e9), int(1e9)
for candidate in candidates:
    result = numbers[0]
    for number, op in zip(numbers[1:], candidate):
        if op == "+":
            result += number
        elif op == "-":
            result -= number
        elif op == "*":
            result *= number
        elif op == "/":
            if result >= 0:
                result //= number
            else:
                result = -1 * result
                result //= number
                result = -1 * result
        else:
            raise Exception("operation Error")
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)
