def main():
    str = input("string: ")
    str2 = str[((len(str)-1)//2+1):] + str[:((len(str)+1)//2)]
    print(str2)
main()