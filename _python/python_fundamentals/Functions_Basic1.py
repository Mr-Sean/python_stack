#1
def a():
    return 5
print(a())

# PREDICT: 5
# ANSWER: 5


#2
def a():
    return 5
print(a()+a())

# PREDICT: 10
# ANSWER: 10


#3
def a():
    return 5
    return 10
print(a())

# PREDICT: 5
# ANSWER: 5


#4
def a():
    return 5
    print(10)
print(a())

# PREDICT: 5
# ANSWER: 5


#5
def a():
    print(5)
x = a()
print(x)

# PREDICT: 5
# ANSWER: 5,NONE


#6*
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

# PREDICT: 3,5,8
# ANSWER: 3,5,NONETYPE ERROR


#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# PREDICT: 25
# ANSWER: 25


#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
	return 10
    return 7
print(a())

# PREDICT: 100,10,7
# ANSWER: 100,10


#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# PREDICT: 7,14,21
# ANSWER: 7,14,21


#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# PREDICT: 8
# ANSWER: 8


#11*
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# PREDICT: 500,300,500,500
# ANSWER: 500,500,300,500


#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# PREDICT: 500,500,300
# ANSWER: 500,500,300,500


#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# PREDICT: 500,500,300,500
# ANSWER: 500,500,300,300


#14*
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# PREDICT: 1,2,3,1
# ANSWER: 1,3,2


#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# PREDICT: 1,10,???
# ANSWER: 1,3,5,10