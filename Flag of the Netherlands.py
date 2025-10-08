import time

RED="\x1b[48;5;1m"
WHITE="\x1b[48;5;255m"
BLUE="\x1b[48;5;27m"
RESET="\x1b[0m"   #Определите красный, белый, синий и сброс цвета с помощью управляющих последовательностей ANSI
flag_length=3
flag_width=50  #Длина и ширина нарисованного флага
for i in range(1,flag_length+1):
   print(f"{RED}{" "*flag_width}{RESET}")
   time.sleep(0.5)     #Нарисовать красную часть флага Финляндии
for i in range(1,flag_length+1):
   print(f"{WHITE}{" "*flag_width}{RESET}")
   time.sleep(0.5)     #Нарисовать белую часть флага Финляндии
for i in range(1,flag_length+1):
   print(f"{BLUE}{" "*flag_width}{RESET}")
   time.sleep(0.5)     #Нарисовать синюю часть флага Финляндии
