strok = input("введите строку для пойска: ")#запрос 
with  open('text.txt', 'r', encoding='utf-8') as file: #открытие файла
    lines = file.readlines()
match_lines = [] #инициализация переменной 
for line in lines: #цикл for
    if strok in line: #оператор if для поиска 
        match_lines.append(line.strip())
print(f"кол-во найденых строк: {len(match_lines)}") #вывод
for line in match_lines: #цикл для вывода line
    print(line)# вывод
sort_line=sorted(match_lines, key=len) #сортировка по длине
print(f"отсортированные строки: {sort_line}")#вывод
for line in match_lines: #цикл для вывода line
    print(line)# вывод
