def main():
    print("int list: [")
    first_l = [int(item) for item in ''.join([char for char in input("    ") if (char.isdigit() or char in {',', '-'})]).split(',') if item.isnumeric()]
    print("]\n")
    
    out = "    "
    for i in range(len(first_l)):
        check = True
        for j in range(i):
            if first_l[i] == first_l[j]:
                check = False
                break
        if check:
            out = out + "YES "
        else:
            out = out + "NO "
    print(out)
main()