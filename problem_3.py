import csv

def main():
    file = open("students.csv")
    while True:
        com = input()
        if com == "СТОП": break
        header = True
        finded = False
        for line in csv.reader(file):
            if header:
                header = False
                continue
            if line[2] == com:
                n, s, o = line[1].split()
                print(f"Проект № {line[2]} делал: {s[0]}. {n} он(а) получил(а) оценку - {line[4]}")
                finded = True
                break

        if not finded:
            print("Ничего не найдено")
    
main()