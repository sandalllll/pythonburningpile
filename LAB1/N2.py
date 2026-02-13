str1 = input('Введите да или нет или что угодно (x2):').lower()
str2 = input().lower()

if ((str1 == 'да') or (str1 == 'нет')) and ((str2 == 'да') or (str2 == 'нет')):
    print('ВЕРНО')
else:
    print('НЕВЕРНО')