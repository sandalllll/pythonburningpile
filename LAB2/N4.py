def main():
    str = input("string: ")
    firsti = str.find('f')
    lasti = str.rfind('f')
    if lasti == -1:
        return
    if firsti == lasti:
        print(firsti)
    else:
        print(f"{firsti}, {lasti}")
main()