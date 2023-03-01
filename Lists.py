# # Create List
# Tạo một danh sách:
thislist = ["apple", "banana", "cherry"]
print(thislist)
# In ra số phần tử trong danh sách:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# Các kiểu dữ liệu chuỗi, int và boolean
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
# Một danh sách với các chuỗi, số nguyên và giá trị boolean:
list1 = ["abc", 34, True, 40, "male"]
# Python - Access List Items
# In mục thứ hai của danh sách
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Lập chỉ mục tiêu cực
# In mục cuối cùng của danh sách
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# Phạm vi chỉ mục
# Trả lại mục thứ ba, thứ tư và thứ năm:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# Phạm vi của các chỉ số tiêu cực
# í dụ này trả về các mục từ "orange" (-4) đến, nhưng KHÔNG bao gồm "xoài" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# Python - Add List Items
# nối các mục
# Sử dụng append()phương pháp để nối thêm một mục
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# Chèn mục
# Chèn một mục vào vị trí thứ hai
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# Mở rộng danh sách
# thêm các phần tử của tropicalvào thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# Python - Change List Items
# Thay đổi giá trị mặt hàng
# Thay đổi mục thứ hai:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# Thay đổi Phạm vi Giá trị Mục
# Thay đổi giá trị "banana" và "cherry" bằng giá trị "blackcurrant" và "watermelon"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Thay đổi giá trị thứ hai và thứ ba bằng cách thay thế bằng một giá trị
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# Chèn mục
# Chèn "dưa hấu" làm mục thứ ba:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# Python - Remove List Items
# Xóa mục được chỉ định
# Xóa "chuối":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# Xóa chỉ mục đã chỉ định
# Xóa mục thứ hai:
# xóa mục cuối bỏ số 1
# xóa mục đầu tiên thay 1 thành 0
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# dùng def để xóa toàn bộ danh sách
thislist = ["apple", "banana", "cherry"]
del thislist
# xóa sạch nội dung trong danh sách vẫn dữ lại danh sách
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# Python - Loop Lists
# Lặp qua một danh sách
# In tất cả các mục trong danh sách, từng mục một:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    # In tất cả các mục, sử dụng một whilevòng lặp để đi qua tất cả các số chỉ mục
    thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
