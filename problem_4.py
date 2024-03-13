import csv, random

def generatePassword():
    """
    Генерация пароля, возвращает пароль
    """
    ans = ""
    for _ in range(8):
        a = random.randint(0, 26*2 + 9)
        if a < 26*2:
            isLower = a < 26
            if isLower:
                ans += chr(65 + a%26).lower()
            else:
                ans += chr(65 + a%26)
        else:
            ans += str(a - 26*2)
    
    return ans

def main():
    """
        Выполнение задание 4
    """
    with open("students_password.csv", mode="w") as write_file:
        with open("students.csv") as file:
            header = True
            for line in csv.reader(file):
                if header:
                    header = False
                    csv.writer(write_file).writerow(line+["login", "password"])
                    continue
                s, n, o = line[1].split()
                csv.writer(write_file).writerow(line+[f"{s}_{n[0]}{o[0]}", generatePassword()])

main()