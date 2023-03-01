# dict
dict = {
    "Ha Noi": "Thang Long ",
    "Hue": "Cung Dinh",
    "Da Nang": "Cau Rong",
    "Ho Chi Minh": "Ben Thanh",
}
for i in dict.keys():
    print(i)
for i in dict.values():
    print(i)
print(dict["Da Nang"])
dict["Da Nang"] = "Cau Han"
dict["Ho Chi Minh"] = [1, 2, 3, 4, 5]
print(dict)
