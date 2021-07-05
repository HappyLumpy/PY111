def print_field(_list):
    for i in range(len(_list)):
          print(_list[i])




def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    field = []
    for i in range(shape[0]):
        field.append([0] * shape[1])
    field[0][0] = 1
    for i in range(len(field)):
        for y in range(len(field[i])):
            if field[i][y] != 0:
                if 0 < i+1 and y+2 < len(field):
                    field[i+1][y+2] += 2
                elif 0 < i + 2 and y + 1 < len(field):
                    field[i + 2][y + 1] += 2
                elif 0 < i + 1 and y - 2 < len(field[i]):
                    field[i + 1][y -2] += 2
                elif 0 < i + 2 and y - 1 < len(field[i]):
                    field[i + 2][y -1] += 2
    return field

if __name__ == '__main__':
    a = calculate_paths((8,8),(8,8))
    print_field(a)