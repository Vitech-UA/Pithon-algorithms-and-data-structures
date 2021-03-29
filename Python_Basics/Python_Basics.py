# Простий if
disaster = False
if disaster:
    print("true!")
else:
    print("false!")

small = True
big = False

# вкладений if
if small:
    if big:
        print("big = true")
    else:
        print("big = false")
else:
    print("Small = false")

# if elif
color = "green"

if color == "red":
    print("red")
elif color == "green":
    print("green")
elif color == "cyan":
    print("cyan")

#додамо трохи логіки
x = 0
y = 4
z = 7

if (x == 0) and (z == 7):
    print("x:0, z:7")

if(z == 7) or (y == 0):
    print("z:7 or y:0")

 
if(z == 7) or not(y == 0):
    print("z:7 or y:!0")

# Цикл while: break
count = 1

while count <= 5:
    print("count")
    if count == 3:
        print("ERROR")
        break
    count+=1


# Цикл while: continue
count = 0
while count <= 9:
    
    count +=1
    if count == 6:
        continue
    print("Count:", count)

# цикл for
# пробіжимось по списку
# ітерування по списку, кортежу повертає один елемент списку або кортежу
rabbits = ['fg', 'pc', 'dp']
for i in rabbits:
    print(i)

# ітерування по строці повертає 1 її символ
stroka = 'hello world'
for ch in stroka:
    print(ch)

# ітерування по словнику, поверне його ключ
py_dict = {1 : 'ivan', 2:'viktor', 3:'oleksa'}
for i in py_dict:
    print(i)

# щоб ітерувати по значеннях треба використати ф-ю values()
for i in py_dict.values():
    print(i)

