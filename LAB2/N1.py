def main():
    str = input("first string: ")
    if len(str) >= 3:
        print(str[2])
    else:
        print("no 3th char")
    
    str = input("second string: ")
    if len(str) >= 2:
        print(str[-2])
    else:
        print("no penultimate char")
    
    #no exceptions thrown
    print(input("thrid string: ")[0:5])
    
    print(input("4th string: ")[0:(len(str)-2)])
    
    print(input("5th string: ")[::2])
    
    print(input("6th string: ")[1::2])
    
    print(input("7th string: ")[-1::-1])
    
    print(input("8th string: ")[-1::-2])
    
    print(len(input("8th string: ")))
main()