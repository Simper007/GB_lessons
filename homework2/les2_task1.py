# 1. Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва

def to_sting(name,age,city):
    print(f'{name}, {age} год(а), проживает в городе {city}')

data=[]
data.append(input('Введите имя: '))
data.append(input('Введите возраст: '))
data.append(input('Введите город проживания: '))

to_sting(data[0],data[1],data[2])