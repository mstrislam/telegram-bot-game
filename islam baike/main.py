'''from helper_functions import is_palindrome
text=input("введите строку :")
if is_palindrome(text):
    print("строка является полендромом")
else:
    print("строка не является полендромом")'''

'''from helper_functions import get_seasen
month= int(input("введите номер  месяца(от 1 до 12) :"))
seasen=get_seasen(month)
print("сезон",seasen)'''

from helper_functions import calculate_sum
from helper_functions import calculate_difference
from helper_functions import calculate_product
from helper_functions import calculate_div
'''chislo1 = int(input("введите первое число"))
chislo2 = int(input("введите второе число"))

operator = input("введите оператор")


if operator == "+":
    summa = calculate_sum(chislo1, chislo2)
    print(summa)
elif operator =="-":
    summa =calculate_difference(chislo1,chislo2)
    print(summa)
elif operator =="*":
    summa = calculate_product(chislo1, chislo2)
    print(summa)
elif operator =="//":
    summa =calculate_div(chislo1,chislo2)
    print(summa)'''

#4
from helper_functions import num
num=int(input("введите четное число"))
if num % 2 == 0:
    print("число четное")
else:
    print("число не  четное")