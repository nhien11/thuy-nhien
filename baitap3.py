str = str(input())
def string(str):
    return [i for i in str.split() if len(i)>3 ]
print(string(str))