import re
from collections import Counter

def main():
    print(dict(Counter([s for s in re.split(r'[. ]', input("One line poem: ")) if s])))
main()
