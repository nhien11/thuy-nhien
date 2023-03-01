#Bạn có thể hiển thị một chuỗi ký tự bằng hàm print():
print("Hello")
print('Hello')
#Việc gán một chuỗi cho một biến được thực hiện với tên biến theo sau là dấu bằng và chuỗi:
a = "Hello"
print(a)
#Chuỗi nhiều dòng
#Bạn có thể gán một chuỗi nhiều dòng cho một biến bằng cách sử dụng ba dấu ngoặc kép:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
#Strings are Arrays
print(a)
#Lấy ký tự ở vị trí 1 (hãy nhớ rằng ký tự đầu tiên có vị trí 0):
a = "Hello, World!"
print(a[1])
#Vì chuỗi là mảng nên chúng ta có thể lặp qua các ký tự trong chuỗi bằng một forvòng lặp
for x in "banana":
  print(x)
  #Để lấy độ dài của một chuỗi, hãy sử dụng len()hàm
  a = "Hello, World!"
print(len(a))
#Python - Slicing Strings
# Lấy các ký tự từ vị trí 2 đến vị trí 5
b = "Hello, World!"
print(b[2:5])
#Nhận các ký tự từ đầu đến vị trí 5
b = "Hello, World!"
print(b[:5])
#Lấy các ký tự từ vị trí 2 và cho đến hết:
b = "Hello, World!"
print(b[2:])
# Nhận các ký tự:
# Từ: "o" trong "Thế giới!" (vị trí -5)
# Tới, nhưng không bao gồm: "d" trong "World!" (vị trí -2):
b = "Hello, World!"
print(b[-5:-2])
#Python - Modify Strings
#Phương upper()thức trả về chuỗi ở dạng chữ hoa
a = "Hello, World!"
print(a.upper())
#Phương lower()thức trả về chuỗi ở dạng chữ thường
a = "Hello, World!"
print(a.lower())
#Phương pháp này strip()loại bỏ bất kỳ khoảng trắng nào từ đầu hoặc cuối:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#Phương replace()thức thay thế một chuỗi bằng một chuỗi khác:
a = "Hello, World!"
print(a.replace("H", "J"))
#Phương split()thức phân tách chuỗi thành các chuỗi con nếu nó tìm thấy các phiên bản của dấu tách:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#Strings are Arrays
#Hợp nhất biến avới biến bthành biến c
a = "Hello"
b = "World"
c = a + b
print(c)
