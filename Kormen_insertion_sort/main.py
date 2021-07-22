input_data = [23, 43, 22, 1, 2, 7, 8, 0, 98, 1999]

for j in range(2, len(input_data)):
    key = input_data[j]
    i = j - 1
    while i >= 0 and input_data[i] > key:
        input_data[i + 1] = input_data[i]
        i = i - 1
    input_data[i + 1] = key
print(input_data)


