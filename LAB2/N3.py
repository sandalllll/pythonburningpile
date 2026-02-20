def main():
    str = input("string: ")
    firsti = str.find('h')
    lasti = str.rfind('h')
    if (lasti - firsti) <= 1:
        print(str)
        return
    print(str[: firsti + 1] + (str[firsti + 1 : lasti])[-1::-1] + str[lasti :])
main()