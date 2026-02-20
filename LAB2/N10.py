def main():
    print("input numbers or something else")
    numbers = []
    while True:
        to_parse = input()
        if not to_parse:
            break
        try:
            to_parse = int(to_parse)
        except ValueError as e:
            break
        numbers.append(to_parse)
    
    for i in range(1, len(numbers)):
        if (numbers[i] > 0 and numbers[i-1] > 0) or (numbers[i] < 0 and numbers[i-1] < 0) or (numbers[i] == 0 and numbers[i-1] == 0):
            print(str(numbers[i - 1]) + ", " + str(numbers[i - 1]))
main()