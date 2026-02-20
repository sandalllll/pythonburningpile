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
    
    for i in range(0, len(numbers)):
        do_qm = True
        for j in range(0, i):
            if numbers[i] == numbers[j]:
                do_qm = False
                break
        if do_qm:
            print(numbers[i])
main()