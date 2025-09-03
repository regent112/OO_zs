import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        raise ValueError('Не указан аргумент "Количество этажей"')
    if len(args) < 3:
        raise ValueError('Не указан аргумент "Путь к файлу"')
    try:
        count_floor = int(args[1])
    except (ValueError, TypeError) as err:
        raise err('Аргумент "Количество этажей" должен быть целым числом')
    if count_floor < 1:
        raise ValueError('Аргумент "Количество этажей" должен быть больше нуля')
    path_to_result = args[2]
    if not path_to_result.endswith('.txt'):
        raise ValueError('Аргумент "Путь к файлу" должен заканчиваться на ".txt"')
    len_line = max(2 + 4 * (count_floor - 1), 5)

    def calc_spaces(len_cur_line: int) -> int:
        count = (len_line - len_cur_line) // 2
        if count_floor % 2 == 0:
            count += 1
        return count

    with open(path_to_result, 'w') as fw:
        fw.write(' ' * calc_spaces(1) + 'W' + '\n')
        fw.write(' ' * calc_spaces(1) + '*' + '\n')
        for floor in range(1, count_floor):
            line = '*' * (4 * floor + 1)
            count_spaces = calc_spaces(len(line))
            if floor % 2 == 1:
                line = '@' + line
                count_spaces -= 1
            else:
                line = line + '@'
            fw.write(
                 ' ' * count_spaces + line + '\n'
            )
        fw.write(' ' * calc_spaces(5) + 'TTTTT' + '\n')
        fw.write(' ' * calc_spaces(5) + 'TTTTT')
