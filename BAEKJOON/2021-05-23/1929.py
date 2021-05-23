# 에라토스테네스의 체
import sys
m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    if i == 2 or i == 3:
        print(i)
    elif i % 2 != 0 and i % 3 != 0:
        print(i)
