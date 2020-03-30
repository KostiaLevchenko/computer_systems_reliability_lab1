from csv import reader


def open_file(path):
    array = []
    with open(path, "r") as csv_file:
        csv_reader = reader(csv_file, delimiter=',')
        for lines in csv_reader:
            array.append(int(lines[0]))
    return array
