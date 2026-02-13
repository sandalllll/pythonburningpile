def main():
    print('Введите пароль (дважды)\n')
    while True:
        p1 = input()
        p2 = input()
        if len(p1) < 8:
            print("Короткий!")
            continue
        if "123" in p1:
            print("Простой!")
            continue
        if p1 != p2:
            print("Различаются!")
            continue
        break
    print("ОК")
main()