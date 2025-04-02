import sys

numL = sys.stdin.read().strip().split("\n")

for i in numL:
    A, B = map(int, i.split())

    if A != 0 and B != 0:
        print(A + B)