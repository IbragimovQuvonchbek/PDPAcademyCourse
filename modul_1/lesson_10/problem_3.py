if __name__ == '__main__':
    try:
        arr = [1, 2, 3, 4, 5]
        print(arr[5])  # IndexError
    except IndexError:
        print("IndexError")

    try:
        dic = {"a": 1, "b": 2}
        print(dic["c"])  # KeyError
    except KeyError:
        print("KeyError")

    try:
        a = 2
        b = "c"
        print(a + b)  # TypeError
    except TypeError:
        print("TypeError")
