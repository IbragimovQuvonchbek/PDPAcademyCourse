if __name__ == '__main__':
    def longest_name(*names) -> str:
        shortest_name = names[0]
        len_name = len(shortest_name)
        for i in range(1, len(names)):
            if len(names[i]) < len_name:
                len_name, shortest_name = len(names[i]), names[i]
        return shortest_name


    print(longest_name("Quvonchbek", "Aslbek", "Nurmuhammad", "Azimjon"))
