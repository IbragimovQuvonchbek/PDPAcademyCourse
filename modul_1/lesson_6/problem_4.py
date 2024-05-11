if __name__ == '__main__':
    words = input("Vergul bilan ajratib so'zlar kiriting: ").split(",")
    target = input("qidirayotgan ism: ")
    index = -1
    for i in range(len(words)):
        if words[i] == target:
            index = i
            break
    print(index)

