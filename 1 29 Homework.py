
# coding: utf-8

# In[1]:

#1)
for i in range(3, 17):
    # 17-3 = 14
    print 'hello'


# In[4]:

#2)
for j in range(12):
    if j % 3 == 0:
        # if j is divisible by 3 (3,6,9,12) = 4x
        print 'hello'


# In[6]:

#3)
for j in range(15):
    if j % 5 == 3:
        # 8, 13 = 2x
       print 'hello'
    elif j % 4 == 3:
        # 7, 11, 15 = 3x
        # = 5x total
       print 'hello'


# In[32]:

#4)
z=0
while z != 15:
    print 'hello'
    z = z + 3
# 0, 3, 6, 9, 12 = 5x


# In[ ]:

# 5)
z = 12
while z < 100:
    if z == 31:
       for k in range(7):
           print 'hello'
    elif z == 18:
        print 'hello'
    z=z+1


# In[1]:

￼# What does fooXX do?
def foo1(x):
    # returns x^0.5
    return x ** 0.5

def foo2(x, y):
    # returns whichever is greater
    if x>y:
        return x
    return y

def foo3(x, y, z):
    # re-orders inputs to least (x) --> greatest (z)
    if x > y:
        tmp = y
        y=x
        x = tmp
    if y > z:
        tmp = z
        z=y
        y = tmp
    if x > y:
        tmp = y
        y=x
        x = tmp
    return [x, y, z]


# In[3]:

def foo4(x):
    #factorial: multiply 1 * 2 * 3... until x
    result = 1
    for i in range(1, x + 1):
       result = result * i
    return result


# In[ ]:

def foo5(x):
    # factorial
    if x == 1:
       return 1
return x * foo5(x - 1)


# In[ ]:



