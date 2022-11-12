"""
a,b = map(int, input().split())

for _ in range(b):
    print('*'*a)
"""
#2022.11.12
a, b = map(int, input().strip().split(' '))

for _ in range(b):
    print('*'*a)
