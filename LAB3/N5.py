import re

def main():
    text = ""
    for i in range(1, int(input("First poem lines count: ")) + 1):
        text = text + input("First poem line no " + str(i) + ": ") + " "
    print(len(set([s for s in re.split(r'[. ]', text) if s])))
main()
