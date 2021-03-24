emty_dict ={} #створюємо пустий словник
print(emty_dict)

radio_component = {"diode" : "BYV26C", "transistor" : "KT315", "suppressor" : "P6KE51" }
print(radio_component)

tuple_ch = ('ab','cd','ef') #оголошую кортеж
print(tuple_ch) #надрукую його

dict_from_tuple = dict(tuple_ch) # Перетворення двохсимвольного кортежу в список
print(dict_from_tuple)

#Додамо ще одну деталь у словник
radio_component["Triaq"] = "BTA12-600"
print(radio_component)

#Оновимо одну деталь у словнику
radio_component["Triaq"] = "BTA41-600"
print(radio_component)

#Об'єднаю два словника
cap = {"capacitor" : "470 uF / 25V"}
radio_component.update(cap)
print(radio_component)

#Видалю зі словника елемент - транзистор
del radio_component['transistor']
print(radio_component)

#Перевірю наявність ключа у словнику
print('transistor' in radio_component)
print('diode' in radio_component)

#Надрукую елемент словника по-ключу, перед цим перевірю чи він існує у словнику
if 'suppressor_' in radio_component:
    print("suppressor : ",radio_component['suppressor'])
else:
    print("Not Found")

#Отримання списку всих ключів
key_list = radio_component.keys()
print(key_list)

#Отримання списку всих значень
value_list = radio_component.values()
print(value_list)

#Отримання списку всих пар ключ-значення
#Поверне список зі списками ключ-значення.
key_value_list = list(radio_component.items())
print(key_value_list)



