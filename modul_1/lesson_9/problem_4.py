if __name__ == '__main__':
    numbers = input("sonlar: ").split()
    result = map(lambda x: x[::-1], numbers)
    print(" ".join(result))
