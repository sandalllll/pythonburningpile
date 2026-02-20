def main():
    queue = []
    while True:
        msg = input()
        if msg == 'x':
            break
        if msg[0] == "К" or msg[0] == "к":
            msg = msg.split(' ')[-1]
            if msg[-1] == '.':
                msg = msg[:-1]
            queue.append(msg)
        elif msg[0] == "Я" or msg[0] == "я":
            msg = msg.split(' ')[-1]
            if msg[-1] == '.':
                msg = msg[:-1]
            queue.insert(0, msg)
        else:
            if len(queue):
                print("Заходит " + queue.pop(0) + "!")
            else:
                print("В очереди никого нет.")
    return
main()