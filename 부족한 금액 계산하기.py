def solution(price, money, count):
    cost = price * (count * (count + 1)) // 2

    answer = cost - money

    if answer < 0:
        return 0

    return answer



if __name__ == '__main__':
    price = 3
    money = 20
    count = 4
    print(solution(price, money, count))