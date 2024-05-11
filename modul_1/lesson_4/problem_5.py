if __name__ == '__main__':
    a = float(input("a kiriting: "))
    if a == 0:
        ilmiy_korinishga = "0"
    else:
        if abs(a) < 1:
            power = 0
            while abs(a) < 1:
                a *= 10
                power -= 1
        else:
            power = 0
            while abs(a) >= 10:
                a /= 10
                power += 1

        if power == 0:
            ilmiy_korinishga = str(a)
        else:
            ilmiy_korinishga = f"{a}*10^{power}"

    print(f"{ilmiy_korinishga}")
