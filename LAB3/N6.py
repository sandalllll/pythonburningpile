from collections import Counter

def main():
    s_names = []
    for i in range(1, int(input("Second names count: ")) + 1):
        s_names.append(input("Second name no " + str(i) + ": "))
    
    out = 0
    for value in dict(Counter(s_names)).values():
        if value > 1:
            out += value
    print(out)
main()
