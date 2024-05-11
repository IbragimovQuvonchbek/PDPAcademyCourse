if __name__ == '__main__':
    words = input("Vergul bilan ajratib so'zlar kiriting: ").split(",")
    target = input("qidirayotgan ism: ")
    times = 0
    for i in range(len(words)):
        if words[i] == target:
            times += 1
    print(times)
