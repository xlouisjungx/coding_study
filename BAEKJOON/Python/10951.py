import sys

data = sys.stdin.read().strip().split("\n")


for line in data:
    A, B = map(int, line.split())
    print(A + B)