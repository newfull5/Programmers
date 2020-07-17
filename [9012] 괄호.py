for _ in range(int(input())):
    a = input()

    for asdf in range(25):
        a = a.replace('()','')
        
    if a == '':
        print('YES')
    else:
        print('NO')
