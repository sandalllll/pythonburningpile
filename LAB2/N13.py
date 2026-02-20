def main():
    numbers = input("throw me some numbers: ")
    words = input("throw me some words: ")
    numbers = [int(item) for item in numbers.split(' ')]
    print(numbers)
    words = words.split(' ')
    str_out = (words[numbers[0] - 1])[:1].upper() + (words[numbers[0] - 1])[1:]
    numbers.pop(0)
    for i in numbers:
        str_out = str_out + " " + words[i - 1].lower()
    print(str_out)
main()