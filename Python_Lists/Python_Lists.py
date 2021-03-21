
weekdays = ['Monday', 'Tuesday','Wednesday','Thursday','Friday'] #створено список днів тижня
print(weekdays) #друкую весь список
print(weekdays[3]) #друкую 3-й елемент зі списку
print(weekdays[-1]) #друкую останній елемент зі списку

weekdays[1] = 'Happy' #змінюю перший елемент списку по(доступ по індексу)
print(weekdays) #вивід модифікованого списку

print(weekdays[0::2]) #вивід преших трьох елементів списку
print(weekdays[::-1]) #вивід список задом на перед

weekdays.append('Zippo') #додаю один елемент в кінець списку
print(weekdays) # вивід модифікованого списку

weekend = ['Saturday','Sunday']

weekdays += weekend
print(weekdays) # вивід модифікованого списку

weekdays.insert(3, 'Three') # додаю один елемент в 3-тю позицію списку
print(weekdays) # вивід модифікованого списку

del weekdays[3] # видаляю 3-й елемент зі списку (del - це оператор пітон, а не матод класу list)
#weekdays.remove('Three') # можна видалити і по значенню.
print(weekdays) # вивід модифікованого списку

a = weekdays.index('Saturday') #знайду індекс елементу по його назві
print(a)

print('Saturday' in weekend) #перевірка чи є у списку 'Saturday'

print(weekdays.count('Saturday')) #перевірка к-ті включень 'Saturday' у списку

weekdays.sort() #сортую список
print(weekdays) # вивід модифікованого списку