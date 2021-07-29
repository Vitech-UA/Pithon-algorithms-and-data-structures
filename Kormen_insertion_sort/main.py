input_data_ = [31, 41, 59, 26, 41, 58]

print("До сортування:   ", input_data_)

# Сортування за зростанням Кормен завдання 2.1.1
for i in range(len(input_data_)):
    k = i
    while k > 0 and input_data_[k - 1] > input_data_[k]:
        tmp = input_data_[k - 1]
        input_data_[k - 1] = input_data_[k]
        input_data_[k] = tmp
        k -= 1
print("Після сортування:", input_data_)

# Сортування за спаданням Кормен завдання 2.1.2
input_data_ = [31, 41, 59, 26, 41, 58]
for i in range(len(input_data_)):
    k = i
    while k > 0 and input_data_[k - 1] < input_data_[k]:
        tmp = input_data_[k - 1]
        input_data_[k - 1] = input_data_[k]
        input_data_[k] = tmp
        k -= 1
print("Після сортування:", input_data_)

# пошук елементу у массиві Кормен завдання 2.1.3
input_data_ = [31, 41, 59, 26, 41, 58]


def search_in_list(key, target_list: list):
    for i in range(len(target_list)):
        if target_list[i] == key:
            print("Знайдено елемент {0} на позиції {1}".format(target_list[i], i))
        else:
            print("Не знайдено такого елементу у списку")
            return


search_in_list(59, input_data_)

# Додавання чисел з двох лістів у третій Кормен завдання 2.1.4
A = [0b11101101, 0b11100100]
B = [0b00101101, 0b01010101]
C = list()

for i in range(0, len(A)):
    C.insert(i, A[i] + B[i])

for i in range(0, len(C)):
    print(bin(C[i]))
