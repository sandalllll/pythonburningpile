def main():
    to_stretch = input("string: ")
    s_len = len(to_stretch)
    s_len_half = (s_len // 2) - 1
    if s_len % 2:
        u = 1
        print(" " * (s_len_half + 1) + to_stretch[s_len_half + 1])
    else:
        u = 0
    for i in range(s_len_half, -1, -1):
        print((" " * i) + to_stretch[i] + (" " * ((s_len_half - i) * 2 + u)) + to_stretch[s_len - 1 - i])
main()