def countNumber():
    strl = "PYnative29@#0496"
    sum = 0
    count = 0
    for a in strl:
        if a.isdigit():#kiem tra cac ki tu
            sum += int(a)
            count += 1
    print(sum)
    print(count)
    print("average of number:", int(sum / count))


countNumber()
