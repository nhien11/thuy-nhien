rows = int(input("Enter Right Pascals Star Triangle Pattern Rows = "))

print("====Right Pascals Star Triangle Pattern====")

for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

for i in range(rows - 1, -1, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()
