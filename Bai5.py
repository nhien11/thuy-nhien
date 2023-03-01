# nterms = 10

# # nạp biến thành phần
# n1, n2 = 0, 1
# count = 0

# # kiểm tra tồn tại số trong dãy không được tồn tại không âm và có sẵn
# if nterms <= 0:
#    print("Vui lòng nhập số tích cực")
# # nếu chỉ có 1 số, in ra số n1
# elif nterms == 1:
#    print("Dãy fibonacci phải được bắt đầu từ ",nterms,":")
#    print(n1)
# # chuyển đổi hệ thống dãy fibonacci
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # cập nhật giá trị
#        n1 = n2
#        n2 = nth
#        count += 1
for i in range(1, 11):
    print(i)
    print("sum", (i - 1) + i)
