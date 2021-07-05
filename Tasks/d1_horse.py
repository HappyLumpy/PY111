def print_field(_list):
    for i in range(len(_list)):
          print(_list[i])




def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    field = []
    for i in range(shape[0]):
        field.append([0] * shape[1])
    field[0][0] = 1
    sum_ = 0
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] != 0:
                if 0 <= y+1 < len(field) and 0 <= x+2 < len(field[y]):
                    field[y+1][x+2] = 2 * field[y][x] + field[y+1][x+2]
                if 0 <= y + 2 < len(field)  and 0 <= x + 1 < len(field[y]):
                    field[y + 2][x + 1] = 2  * field[y][x] + field[y + 2][x + 1]
                if 0 <= y + 1 < len(field) and 0 <= x - 2 < len(field[y]):
                    field[y + 1][x -2] = 2  * field[y][x] + field[y + 1][x -2]
                if 0 <= y + 2 < len(field) and 0 <= x - 1 < len(field[y]):
                    field[y + 2][x -1] = 2  * field[y][x] + field[y + 2][x -1]
    return field[point[0]][point[1]]


if __name__ == '__main__':
    a = calculate_paths((8,8),(7,7))
    print(a)
