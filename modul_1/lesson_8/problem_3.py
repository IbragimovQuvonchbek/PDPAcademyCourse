if __name__ == '__main__':
    def longest_name(*names):
        longest_name = ""
        len_name = 0
        for name in names:
            if len(name) > len_name:
                len_name, longest_name = len(name), name
        return longest_name


    print(longest_name("Quvonchbek", "Nurmuhammad", "Azimjon"))
