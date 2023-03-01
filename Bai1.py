list = [1, 2, 10, 6, 55, 91, 2, 24]
max = list[0]
for a in range(len(list)):
    if list[a] > max:
        max = list[a]
print(max)
min = list[0]
for a in range(len(list)):
    if list[a] < min:
        min = list[a]
print(min)
# sắp xếp tăng dần
for a in range(len(list)):# lap cac pt trong list
    for b in range(a, len(list)): #lap cac phan thu phia sau
        if list[a] > list[b]:
            t = list[a]
            list[a] = list[b]
            list[b] = t
print(list)
# sắp xếp giảm dần
for a in range(len(list)):
    for b in range(a, len(list)):
        if list[a] < list[b]:
            t = list[a]
            list[a] = list[b]
            list[b] = t
print(list)
# in ra số chẵn
a = 0
for a in list:
    if a % 2 == 0:
        print(a, end=" ")
print("\n")
# in ra số lẽ
a = 0
for a in list:
    if a % 2 != 0:
        print(a, end=" ")
print("\n")
