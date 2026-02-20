def main():
    while True:
        str = input("first word: ")
        if str:
            break
    last_char = str[-1]
    while True:
        str = input()
        if not str:
            continue
        if str[0] == last_char:
            last_char = str[-1]
        else:
            break
    print(str)
main()