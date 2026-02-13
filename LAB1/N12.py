def main():
    try:
        h = int(input())
    except ValueError as e:
        print("Wasted")
        return None
    nlcount = 0
    nlnow = 0
    out = ""
    for i in range(1, h+1):
        if nlnow > 0:
            out = out + str(i) + " "
            nlnow = nlnow - 1
        else:
            nlcount = nlcount + 1
            nlnow = nlcount
            out = out + str(i) + "\n"
    print(out)
main()
