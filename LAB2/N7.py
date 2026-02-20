def main():
    path = input("path: ")
    draw_sym = path[0]
    x_pos = 0
    path = path[1:] + "V"
    while True:
        hor_dist = path.find('V')
        if hor_dist == -1:
            break
        tmp_str = ""
        if path[0] == '>':
            for i in range(0, x_pos):
                tmp_str = tmp_str + " "
            for i in range(0, hor_dist + 1):
                tmp_str = tmp_str + draw_sym
            x_pos = x_pos + hor_dist
        else:
            for i in range(0, x_pos - hor_dist):
                tmp_str = tmp_str + " "
            for i in range(0, hor_dist + 1):
                tmp_str = tmp_str + draw_sym
            x_pos = x_pos - hor_dist
        print(tmp_str)
        path = path[hor_dist + 1 :]
main()