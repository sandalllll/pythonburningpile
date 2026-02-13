def main():
    nmbs = input('Введите четырехзначное число: ')
    
    if (len(nmbs) != 4) or (not nmbs.isnumeric()):
        print("Wasted")
        return
    
    nmb = int(nmbs)
    if nmb < 1000:
        print("Wasted")
        return
    
    d0 = nmb % 10
    d1 = nmb // 10 % 10
    d2 = nmb // 100 % 10
    d3 = nmb // 1000
    
    if d1 < d0 and d1 != 0:
        d0, d1 = d1, d0
    if d2 < d0 and d2 != 0:
        d0, d2 = d2, d0
    if d3 < d0 and d3 != 0:
        d0, d3 = d3, d0
    
    if d2 < d1:
        d1, d2 = d2, d1
    if d3 < d1:
        d1, d3 = d3, d1
    
    if d3 < d2:
        d2, d3 = d3, d2
    
    print(d0 * 1000 + d1 * 100 + d2 * 10 + d3)

main()