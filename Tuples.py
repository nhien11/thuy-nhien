# Create Tuples
#tạo một tp
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#In ra số phần tử trong tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#Python - Access Tuple Items
#In mục thứ hai trong tuple:chỉ mục tiêu cực -1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Thay đổi giá trị Tuple
#Chuyển đổi bộ dữ liệu thành danh sách để có thể thay đổi nó
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
# Thêm tuple vào tuple . Bạn được phép thêm các bộ vào các bộ, vì vậy nếu bạn muốn thêm một mục, (hoặc nhiều mục), hãy tạo một bộ mới với (các) mục đó và thêm nó vào bộ hiện có:

# Ví dụNhận máy chủ Python của riêng bạn
# Tạo một bộ dữ liệu mới với giá trị "orange" và thêm bộ dữ liệu đó:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#xóa mục
# Chuyển đổi bộ dữ liệu thành danh sách, xóa "apple" và chuyển đổi lại thành bộ dữ liệu:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#Python - Unpack Tuples
#Đóng gói một tuple
fruits = ("apple", "banana", "cherry")
#Giải nén một tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#Python - Loop Tuples
# Lặp lại các mục và in các giá trị:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#   In tất cả các mục, sử dụng một whilevòng lặp để đi qua tất cả các số chỉ mục:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1