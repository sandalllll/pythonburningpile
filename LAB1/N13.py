def main():
    try:
        x = int(input())
        y = int(input())
    except ValueError as e:
        print("Wasted")
        return None
    symb = input()
    if len(symb) != 1:
        Print("Wasted")
        return
    out1 = ""
    out2 = symb
    for i in range(x):
        out1 = out1 + symb
    for i in range(x - 2):
        out2 = out2 + ' '
    out2 = out2 + symb
    print(out1)
    for i in range(y - 2):
        print(out2)
    print(out1)
main()
