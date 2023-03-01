# str ="Emma is good developer. Emma is a writer"
# count = {}
# x=0
# for i in str:
#     if i in count:
#         count[i] +=1
#     else:
#         count[i] = 1

# print(count)


def word_count(str):
    counts = dict()
    words = str.split()#split là thức tách 1 chuỗi thành 1 danh sách mỗi từ là 1 mục danh sách

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
print(word_count("Emma is good developer. Emma Emma is a writer Emma"))
# def countString2():
#     string = 'Emma is good developer. Emma is a writer'
#     splitChar = string.split(" ")
#     countChar = Counter (splitChar)
#     print( countChar.most_common(1))
# countString2()
