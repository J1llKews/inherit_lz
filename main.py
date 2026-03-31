from poker import Texas_holdem, Omaha_holdem

def main():
    print("выберите режим игры")
    print("1 - texas hold'em")
    print("2 - omaha hold'em")

    choice = input("ваш выбор: ")

    if choice == "1":
        print("\ntexas hold'em")

        a1 = input("введите значение первой карты: ")
        m1 = input("введите масть первой карты: ")

        a2 = input("введите значение второй карты: ")
        m2 = input("введите масть второй карты: ")

        t = Texas_holdem(a1, m1, a2, m2)
        t.pocket_info()
        t.win_chance()

    elif choice == "2":
        print("\nomaha hold'em")

        a1 = input("введите значение 1й карты: ")
        m1 = input("введите масть 1й карты: ")

        a2 = input("введите значение 2й карты: ")
        m2 = input("введите масть 2й карты: ")

        a3 = input("введите значение 3й карты: ")
        m3 = input("введите масть 3й карты: ")

        a4 = input("введите значение 4й карты: ")
        m4 = input("введите масть 4й карты: ")

        o = Omaha_holdem(a1, m1, a2, m2, a3, m3, a4, m4)
        o.pocket_info()
        o.win_chance()

    else:
        print("неверно")


main()
