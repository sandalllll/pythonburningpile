def main():
    points = [[1, 3], [5, 6], [7, 1], [8, 4], [3, 5], [1, 2], [3, 4], [6, 1]]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1x = points[i][0]
            p1y = points[i][1]
            p2x = points[j][0]
            p2y = points[j][1]
            
            if p1x == p2x or p1y == p2y or abs(p1x - p2x) == abs(p1y - p2y):
                print("YES")
                return
    print("NO")
    return
main()