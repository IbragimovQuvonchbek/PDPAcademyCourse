if __name__ == '__main__':
    a = int(input())
    b = int(input())

    max_num = max(a, b)
    min_num = a + b - max_num

    while min_num != 0:
        max_num, min_num = min_num, max_num % min_num

    print(max_num)
