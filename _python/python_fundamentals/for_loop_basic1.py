# 1
for x in range(151):
    print(x)


# 2
for x in range(5, 1001, 5):
    print(x)


# 3
for num in range(1, 101, 1):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)


# 4
sum = 0
for x in range(1,500000,2):
    sum += x
print(sum)


# 5
for x in range(2018, 0, -4):
    print(x)


# 6
lownum = 1
highnum = 31
mult = 6
for x in range(lownum, highnum+1):
    if x % mult == 0:
        print(x)