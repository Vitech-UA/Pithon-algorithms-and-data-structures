empty_tuple = ()
print(empty_tuple)


mark_tuple = ('Groucho','Chico','Harpo')
print(mark_tuple)

a,b,c = mark_tuple #Розпаковка кортежа, кожній змінній присвоюється елемент кортежу
print(a)
print(b)
print(c)


mark_list = ['One', 'Two', 'Tree']
print(mark_list) #Виведеться, як список
tuper_from_list = tuple(mark_list) #Перетворюємо у кортеж дані передані у функцію tuple
print(tuper_from_list) #Виведеться, як кортеж