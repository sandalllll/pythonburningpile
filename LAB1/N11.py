def main():
    try:
        h = int(input())
    except ValueError as e:
        print("Wasted")
        return None
    for i in range(h):
        str = ""
        for j in range(h - i - 1):
            str = str + " "
        for j in range(i * 2 - 1):
            str = str + "*"
        print(str)
main()