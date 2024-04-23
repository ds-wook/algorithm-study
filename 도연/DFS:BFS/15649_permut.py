import sys
from itertools import permutations
input = sys.stdin.readline
n,m = map(int, input().split())

com = list(permutations(range(1,n+1),m))
for c in com:
	print(*c, sep=' ')