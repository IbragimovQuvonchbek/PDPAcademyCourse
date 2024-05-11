if __name__ == '__main__':
    words = input("so`zlarni kiriting: ").split()
    w1 = list(words[0])
    w2 = [ch for ch in words[1]]
    if len(w1) == len(w2):
        result = True
        index = 0
        while index != len(w1) and len(w2) != 0:
            if w1[index] in w2:
                w2.remove(w1[index])
                index += 1
            else:
                result = False
                break
        print(result)
    else:
        print(False)
