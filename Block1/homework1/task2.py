# 2. Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в
# степень 2 и выведите на экран

while True:
    number = int(input('Введите число больше 0, но меньше 10: '))
    if number > 0 and number < 10:
        print(number**2)
        break
    else:
        print('Неверное число, попробуйте снова')
