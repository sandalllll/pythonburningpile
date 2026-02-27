def main():
    print("int list: [")
    first_l = [int(item) for item in ''.join([char for char in input("    ") if (char.isdigit() or char in {',', '-'})]).split(',') if item.isnumeric()]
    print("]\n")
    
    print(len(set(first_l)))
main()
