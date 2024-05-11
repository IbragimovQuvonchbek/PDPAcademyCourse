from random import randint


def run() -> None:
    random_num = randint(1, 10)
    life = 2
    while life > 0:
        try:
            print(f"Imkoniyatlar soni: {life}")
            a = int(input("son kiriting: "))
            if a == random_num:
                print("Siz o`ylangan sonni topdingiz")
                return
            elif a > random_num:
                print(f"o'ylangan son {a} dan kichik")
            elif a < random_num:
                print(f"o'ylagan son {a} dan katta")
            life -= 1
        except ValueError:
            print("Faqat 1 dan 10 oraliqdagi son kiriting")

    print(f"Sizda imkoniyatingiz qolmadi o'ylangan son -> {random_num}")


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print("\ndastur to'xtatildi!")
