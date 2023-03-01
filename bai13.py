#Initial list
res = []

# Input lengths
len = int(input())

# Add element
for i in range(len):
    # Input elements
    n = str(input())
    res.append(n)

print(int(''.join(res)))
