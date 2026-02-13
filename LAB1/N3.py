while True:
    logn = input('Введите логин: ')
    mail = input('Введите резервный адрес: ')
    if (logn.count('@') == 0) and (mail.count('@') == 1):
        print('ВЕРНО')
        break;
    else:
        print('НЕВЕРНО')