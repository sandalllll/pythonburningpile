nmbs = input('Введите красивое число: ')
isB = True

if len(nmbs) != 3:
    isB = False
if isB and not nmbs.isnumeric():
    isB = False

if isB:
    nmbs2 = sorted(nmbs)
    if (int(nmbs2[0]) + int(nmbs2[2])) != (int(nmbs2[1]) * 2):
        isB = False

if isB:
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')