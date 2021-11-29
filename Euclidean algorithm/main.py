print("Euclidean algorithm")
# Гірша реалізація:
a = int(input())
b = int(input())
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)

# Краща (ефективніша) реалізація:
a = int(input())
b = int(input())
while b > 0:
    c = a % b
    a = b
    b = c
print(a)
