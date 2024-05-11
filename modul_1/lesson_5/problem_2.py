if __name__ == '__main__':
    a = int(input())
    if a % 15 == 0:
        print("FizBiz")
    elif a % 5 == 0:
        print("Biz")
    elif a % 3 == 0:
        print("Fiz")
    else:
        print(a)
