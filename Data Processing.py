RED = '\u001b[41m'
RESET = '\u001b[0m'
sum_odd=0    #Использовать sum_odd для хранения суммы модулей чисел на нечётных позициях
sum_even=0   #Используйте sum_even для хранения суммы абсолютных значений чисел на чётных позициях
with open("C:/Users/超级飞龙/Desktop/sequence.txt.txt", 'r') as file:#Открыть файл
    numbers = [float(number) for number in file]#Преобразовать число в тип с плавающей запятой
    for index,number in enumerate(numbers, start=1):#Используйте enumerate для индексирования чисел в numbers
        abs_number=abs(number)     #Использовать abs для получения абсолютного значения числа
        if index % 2 == 1:       #обозначает, что число находится на нечетной позиции
            sum_odd += abs_number
        else:
            sum_even += abs_number
percent_odd=round(sum_odd/(sum_odd+sum_even)*100)
percent_even=round(sum_even/(sum_odd+sum_even)*100)
REDBOX = f"{RED}  {RESET}"
BLACKBOX = '  '
print("percent_odd: ",str(percent_odd)+"%",end=" ")
for i in range(1,percent_odd+1):       #Напечатайте цветные блоки соответствующей длины в процентах
    print(REDBOX,end="")
print()
print()
print("percent_even:",str(percent_even)+"%",end=" ")
for j in range(1,percent_even+1):
    print(REDBOX,end="")
