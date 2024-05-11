if __name__ == '__main__':
    def reverse_name(name: str) -> None:
        reversed_name = reverse_string(name)
        print(reversed_name)


    def reverse_string(s) -> str:
        if len(s) == 0:
            return s
        else:
            return reverse_string(s[1:]) + s[0]


    if __name__ == "__main__":
        reverse_name(input("Ismingizni kiriting: "))
