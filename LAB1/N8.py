def main():
    print('Ввдите возраста или "!"\n')
    
    count = 0
    minh = 190
    maxh = 150
    
    while True:
        val = input()
        if val == "!":
            break
        if val.isnumeric():
            l = int(val)
            if l < 150 or l > 190:
                continue
            count = count + 1
            if l < minh:
                minh = l
            if l > maxh:
                maxh = l
    
    print(count)
    if count > 0:
        print(str(minh) + " " + str(maxh))

main()