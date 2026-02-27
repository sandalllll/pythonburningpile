def main():
    files = {}
    for i in range(1, int(input("Files count: ")) + 1):
        file_info = input("File no " + str(i) + " with it's rights: ").split(' ')
        if len(file_info) < 2:
            continue 
        file = file_info.pop(0)
        files[file] = 0
        for right in file_info:
            match right:
                case "R":
                    files[file] |= 1
                case "W":
                    files[file] |= 2
                case "X":
                    files[file] |= 4
    
    print(files)
    
    for i in range(1, int(input("Attempts count: ")) + 1):
        command = input("Attempt no " + str(i) + "'s command: ").split(' ')
        if len(command) != 2:
            continue
        file = command[1]
        command = command[0]
        if command in {"read", "write", "execute"}:
            if file in files:
                match command:
                    case "read":
                        if (files[file] & 1):
                            print("OK")
                        else:
                            print("Access denied")
                    case "write":
                        if (files[file] & 2) > 0:
                            print("OK")
                        else:
                            print("Access denied")
                    case "execute":
                        if (files[file] & 4) > 0:
                            print("OK")
                        else:
                            print("Access denied")
            else:
                print("File not found")
        else:
            print("Unknown command")
main()
