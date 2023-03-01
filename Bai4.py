j = []
for i in range(2000, 3200):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i)) #append nối 1 phần tử vào danh sách
print(",".join(j))#join lấy tất cả các mục trong lần lặp vài nối chúng lại thành 1 chuỗi
