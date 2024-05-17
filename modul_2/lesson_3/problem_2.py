class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


if __name__ == '__main__':
    print(Calculator.add(1, 2))  # 3
    print(Calculator.subtract(1, 2))  # -1
    print(Calculator.multiply(1, 2))  # 2
    print(Calculator.divide(1, 2))  # 0.5
