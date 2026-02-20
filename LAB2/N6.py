def main():
    str_1 = input("string: ")
    str_2 = ""
    for i in range(0, len(str_1)):
        for j in range(0, i + 1):
            str_2 = str_2 + str_1[i]
    print(str_2)
main()