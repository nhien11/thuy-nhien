#if tuyên bố:
a = 33
b = 200
if b > a:
  print("b is greater than a")
# Từ khóa elif là cách nói của Python "nếu các điều kiện trước đó không đúng, thì hãy thử điều kiện này".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  #Trong ví dụ này a bằng b , vì vậy điều kiện đầu tiên không đúng, nhưng điều kiện elif là đúng, vì vậy chúng tôi in ra màn hình rằng "a và b bằng nhau"
  #else
  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  #Kiểm tra nếu alớn hơn b, VÀ nếu c lớn hơn a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#ỏ
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")