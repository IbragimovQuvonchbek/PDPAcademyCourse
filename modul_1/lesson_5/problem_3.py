if __name__ == '__main__':
    print("ax^2 + bx + c = 0")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    d = b ** 2 - 4 * a * c
    print(f"{a}x^2 + {b}x + {c} = 0")

    if d == 0:
        print("Tenglama 1ta yechimga ega")
    elif d > 0:
        print("Tenglama 2ta yechimga ega")
    else:
        print("Tenglama 0ta yechimga ega")
