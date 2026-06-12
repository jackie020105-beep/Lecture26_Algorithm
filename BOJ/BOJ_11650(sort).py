# 10814번 (나이순 정렬)
def coordinate_sort():
    dot_no = int(input())
    coordinate_x_y = []
    for _ in range(dot_no):
        x, y = input(f'x와 y의 값을 입력하시오 : ').split()
        coordinate_x_y.append([int(x), int(y)])
    coordinate_x_y.sort(key=lambda dot: (dot[0], dot[1]))
    
    for x_y in range(0, dot_no):
        print(coordinate_x_y[x_y][0], coordinate_x_y[x_y][1])

coordinate_sort()