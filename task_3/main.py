import os


def reader_file(path_to_file: str) -> str:
    """Читает данные из файла"""
    with open(path_to_file, encoding='utf-8') as text_file:
        return text_file.read()


def counter_lines(path_to_file: str) -> int:
    """Считает количество строк в файле"""
    with open(path_to_file, encoding='utf-8') as text_file:
        return len(text_file.readlines())


def sorted_writing_file(target_file: str, source_file: str, total_lines_source_file: int) -> None:
    """Записывает данные в файл"""
    file_name = source_file.split('\\')[-1]
    data = reader_file(source_file)

    if os.path.exists(target_file):
        with open(target_file, 'a', encoding='utf-8') as write_file:
            write_file.write(f'{file_name}\n{total_lines_source_file}\n{data}\n')
    else:
        with open(target_file, 'w', encoding='utf-8') as write_file:
            write_file.write(f'{file_name}\n{total_lines_source_file}\n{data}')


if __name__ == '__main__':
    file_1, file_2, file_3 = '1.txt', '2.txt', '3.txt'
    path_dir = os.getcwd()
    result_file = 'result.txt'
    counter_lines_list = {}

    for file in (file_1, file_2, file_3):
        total_lines = counter_lines(os.path.join(path_dir, file))
        counter_lines_list[file] = total_lines

    for value in sorted(counter_lines_list.values()):
        for key in counter_lines_list:
            if counter_lines_list[key] == value:
                sorted_writing_file(os.path.join(path_dir, result_file), os.path.join(path_dir, key), value)
