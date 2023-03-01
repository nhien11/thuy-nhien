#Tạo và in từ điển
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# In giá trị "thương hiệu" của từ điển:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
# Các giá trị trùng lặp sẽ ghi đè lên các giá trị hiện có:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
# In số mục trong từ điển:

print(len(thisdict))
#Python - Access Dictionary Items
#lấy giá trị của khóa "mustang"
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#c2
x = thisdict.get("model")
# Thêm một mục mới vào từ điển gốc và xem danh sách khóa cũng được cập nhật:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
# Lấy danh sách các giá trị:

x = thisdict.values()
#Phương thức này items()sẽ trả về từng mục trong từ điển, dưới dạng các bộ trong danh sách.
#Python - Change Dictionary Items
#Thay đổi "năm" thành 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
#Cập nhật "năm" của xe bằng phương update() pháp:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
#Python - Add Dictionary Items
#thêm mục
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#Thêm một mục màu vào từ điển bằng phương update() pháp:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
#Python - Remove Dictionary Items
#Phương pop()thức xóa mục có tên khóa được chỉ định:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#lm trống từ điển

thisdict.clear()
#Loop Through a Dictionary
#In tất cả các tên khóa trong từ điển, từng cái một:
for x in thisdict:
  print(x)
  #In tất cả các giá trị trong từ điển, từng cái một:
for x in thisdict:
  print(thisdict[x])
  #Bạn cũng có thể sử dụng values()phương thức này để trả về các giá trị của từ điển:
for x in thisdict.values():
  print(x)
  #Bạn có thể sử dụng keys()phương thức để trả về các khóa của từ điển:
for x in thisdict.keys():
  print(x)
  #Lặp qua cả khóa và giá trị bằng cách sử dụng items()phương thức:
for x, y in thisdict.items():
  print(x, y)
  #Sắp xếp theo key | phương thức keys()
  dict = {1:'red', 2:'blue', 3:'yellow'}
keys_sorted1 = sorted(dict)
print(keys_sorted1)

#>> [1, 2, 3]
#Sắp xếp theo value | phương thức values(
dict = {1:'red', 2:'blue', 3:'yellow'}
values_sorted = sorted(dict.values())
print(values_sorted)

#>> ['blue', 'red', 'yellow']
 #Sắp xếp theo cả key và value | phương thức items()
dict = {1:'red', 2:'blue', 3:'yellow'}
items_sorted = sorted(dict.items())
print(items_sorted)

#>> [(1, 'red'), (2, 'blue'), (3, 'yellow')]
#Sắp xếp dictionary python theo thứ tự giảm dần | hàm sorted()
dict = {1:'red', 2:'blue', 3:'yellow'}
keys_sorted1 = sorted(dict, reverse=True)
print(keys_sorted1)
#valu

dict = {1:'red', 2:'blue', 3:'yellow'}
values_sorted = sorted(dict.values(), reverse=True)
print(values_sorted)

#>> ['yellow', 'red', 'blue']
#theo cả 2
dict = {1:'red', 2:'blue', 3:'yellow'}
items_sorted = sorted(dict.items(), reverse=True)
print(items_sorted)

#>> [(3, 'yellow'), (2, 'blue'), (1, 'red')]
