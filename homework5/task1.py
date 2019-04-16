'''
Решить с помощью генераторов списка.
1. Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
    Примечание: Списки фруктов создайте вручную в начале файла.
'''

fruit_list1 = ['Яблоко', 'Банан', 'Апельсин', 'Ананас', 'Киви']
fruit_list2 = ['Киви','Мандарин', 'Яблоко', 'Слива']

common_list = [fruit for fruit in fruit_list1 if fruit in fruit_list2]

print(common_list)