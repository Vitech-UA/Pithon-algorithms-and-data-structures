input_data_ = [12, 0, 3, 43, 22, 1, 2, 23, 7, 8, 0, 98, 1999]

print("До сортування:   ", input_data_)
for i in range(len(input_data_)):
    k = i
    while k > 0 and input_data_[k - 1] > input_data_[k]:
        tmp = input_data_[k - 1]
        input_data_[k - 1] = input_data_[k]
        input_data_[k] = tmp
        k -= 1
print("Після сортування:", input_data_)
