
weekdays = ['Monday', 'Tuesday','Wednesday','Thursday','Friday'] #створено список днів тижня
print(weekdays) #друкую весь список
print(weekdays[3]) #друкую 3-й елемент зі списку
print(weekdays[-1]) #друкую останній елемент зі списку

weekdays[1] = 'Happy' #змінюю перший елемент списку по(доступ по індексу)
print(weekdays) #вивід модифікованого списку

print(weekdays[0::2]) #вивід преших трьох елементів списку
print(weekdays[::-1]) #вивід список задом на перед