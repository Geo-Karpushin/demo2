import csv

def insertion(data):
    """
    Функция сортировки вставками

    Параметры:
    data - массив с учениками, в которых 5 по счёту элемент - оцена вида int
    """
    for i in range(len(data)):
        j = i - 1 
        key = data[i]
        while data[j][4] < key[4] and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def read_file(filepath):
    """
        Функция считывает данные из файла по соответсвующему пути в формате csv. Возвращает массив словарей с данными, в которых оценка представлена в виде int, а None заменено на -1

        Параметры:
        filepath - имя файла
    """
    content = []
    with open(filepath) as file:
        header = True
        for line in csv.reader(file):
            if header:
                header = False
                continue
            if line[4] == "None": line[4] = -1
            else: line[4] = int(line[4])
            content.append(line)
    
    return content

def main():
    """
    Функция-активатор. Вызывает весь остальной код
    """
    students = read_file("students.csv")

    students = insertion(students)

    i = 1

    j = 0

    print("10 класс:")

    while i != 4:
        if "10" in students[j][3]:
            n, s, o = students[j][1].split()
            print(f"{i} место: {s[0]}. {n}")
            i+=1
        j += 1
    
main()