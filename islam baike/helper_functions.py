
'''def is_palindrome(text: str) -> bool:
  ''это функция находит палиндром''
  text = text.replace("", "")
  return text == text[::-1]'''

#функция находит времена года
'''def get_seasen(month: int)->str:
    if month in (12, 1, 2):
        print("зима")
    elif month in (11, 3, 4):
        print("весна")
    elif month in (10, 3, 5):
        print("лето")
    elif month in (9, 4, 6):
        print("осень")
    else:
        print("такого сезона нету")'''

'''def calculate_sum(number1, number2):
    result = number1 + number2
    return result


def calculate_difference(number1, number2):
    result = number1 - number2
    return result


def calculate_product(number1, number2):
    result = number1 * number2
    return result


def calculate_div(number1, number2):
    result = number1 / number2
    return result'''
def num(num: int)->str:
    num=int(input("введите четное число"))
    if num % 2 == 0:
        print("число четное")
    else:
        print("число не  четное")