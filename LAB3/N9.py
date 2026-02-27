def main():
    votes = {}
    for i in range(1, int(input("States count: ")) + 1):
        state_choise = input("State no " + str(i) + " candidate and votes: ").split(' ')
        if len(state_choise) == 2 and state_choise[1].isnumeric():
            if not (state_choise[0] in votes):
                votes[state_choise[0]] = 0
            votes[state_choise[0]] += int(state_choise[1])
    
    for key in sorted(votes):
        print(key + " " + str(votes[key]))
main()
