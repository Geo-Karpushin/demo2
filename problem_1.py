import csv


def read_line(line):
    """
        Функция распределяет данные из массива в словарь

        Параметры:
        line - данные в виде массива (списка)
    """
    return {
        "id": line[0],
        "name": line[1],
        "titleProject_id": line[2],
        "class": line[3],
        "score": line[4]
    }


def read_file(filepath):
    """
        Функция считывает данные из файла по соответсвующему пути в формате csv. Возвращает заголовоки столбцов в формате строки и массив словарей с данными

        Параметры:
        filepath - имя файла
    """
    header, content = "", []
    with open(filepath) as file:
        for line in csv.reader(file):
            if header == "": 
                header = line
                continue
            content.append(read_line(line))
    
    return header, content

def write_file(header, students, avg):
    """
    Функция записывает результат работы программы в соответствующий файл

    header - заголовки столбцов
    students - массив словарей с данными о проектах
    avg - среднее значение оценки
    """

    with open("student_new.csv", mode="w") as file:
        csv.writer(file).writerow(header)
        for student in students:
            if student["score"] == "None":
                student["score"] = str(avg)
            csv.writer(file).writerow(student.values())


def main():
    """
    Функция-активатор. Вызывает весь остальной код
    """
    header, students = read_file("students.csv")

    score_sum = 0
    counted = 0

    for student in students:
        if student["score"] != "None":
            score_sum += int(student["score"])
            counted += 1
        if "Хадаров Владимир" in student["name"]:
            print("Ты получил " + student["score"] + " за проект – " +student["titleProject_id"])

    avg = f"{(score_sum/counted).__round__(3)}"

    write_file(header, students, avg)


    
main()