def float_range(begin, end, step):
    while begin < end:
        yield begin
        begin += step


if __name__ == '__main__':
    for i in float_range(0, 2, 0.5):
        print(i)
