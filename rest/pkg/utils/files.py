def read_file_lines(file_name: str):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_file(file_name: str):
    f = open(file_name, 'r')
    lines = f.read()
    f.close()
    return lines
