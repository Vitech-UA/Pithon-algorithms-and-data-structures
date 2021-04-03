
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

print(len(weekdays)) #друкую довжину списку

# робота зі списками списків.

def get_average_value(list_data):
    
    if list_data[len(list_data) % 2] > 0:
        return list_data[(len(list_data) // 2)]
    elif list_data[len(list_data) % 2] == 0:
         return list_data[(len(list_data) // 2) + 1]

def get_average_index(list_data):
    return len((list_data) // 2)

plots = list()
voltages = list()
currents = list()

plots = [voltages, currents]
print(plots) # emty

voltages = [1.45, 1.445, 1.98, 1.34, 1.0001, 1.00009, 1.0]
currents = [2.54, 2.64, 2.12, 2.34, 2.99]
plots = [voltages, currents]
print(plots)

voltages.sort()
currents.sort()
print(plots)
current = get_average_value(currents)
voltage = get_average_value(voltages)

print("Current: %.3f" % current, "A")
print("Voltage: %.3f" % voltage, "V")
