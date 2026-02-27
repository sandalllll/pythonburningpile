def main():
    print("first int list: [")
    first_l = [int(item) for item in ''.join([char for char in input("    ") if (char.isdigit() or char in {',', '-'})]).split(',') if item.isnumeric()]
    print("]")
    print("second int list: [")
    second_l = [int(item) for item in ''.join([char for char in input("    ") if (char.isdigit() or char in {',', '-'})]).split(',') if item.isnumeric()]
    print("]")
    print(sorted(set(first_l) & set(second_l)))
main()