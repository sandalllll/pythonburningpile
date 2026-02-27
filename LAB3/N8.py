def main():
    synonyms = {}
    for i in range(1, int(input("Synonym pares count: ")) + 1):
        pare = input().split(' ')
        if len(pare) == 2:
            synonyms[pare[0]] = pare[1]
    word = input("Word to match: ")
    
    for key, value in synonyms.items():
        if (word == key):
            print(value)
            break
        if (word == value):
            print(key)
            break
main()
