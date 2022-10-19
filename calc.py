#Жоский калькулятор

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print( Fore.BLACK )
print( Back.GREEN )

what = input("Что делаем: (+, -, *, /): ")

print( Back.CYAN )

a = float(input("Выберите первое число: "))
b = float(input("Выберите второе число: "))

print( Back.MAGENTA )


if what == ("+"):
    c = a + b
    print("Результат: " + str(c))
elif what == ("-"):
    c = a - b
    print("Результат: " + str(c))
elif what == ("*"):
    c = a * b
    print("Результат: " + str(c))
elif what == ("/"):
    c = a / b
    print("Результат: " + str(c))
else:
    print("Ошибка")

input()    
