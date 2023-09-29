def getsq(num):
    return num*num
    
for j in [1,2,3,4]:
    result = getsq(j)
    print('square of',j,'=',result)
    
    
print('*****************************')

def addnum(a=3,b=4):
    sum=a+b
    print('sum: ',sum)
    
addnum(a=1,b=2)

addnum(b=2)

addnum()

print('**********************************')

def display_name(firstname,lastname,middlename):
    print('first name is :  ',firstname)
    print('lastname is : ', lastname)
    print('middle name: ',middlename)
    
display_name(lastname='Francis', firstname='Divya',middlename='P')

print('*************************************')

def findsum(*numbers):
    result=0
    
    for num in numbers:
        result=result+num
        
    print('sum =',result)
        
findsum(1,1,1,1)

print('***************************')

greet_user= lambda name:print('my name is', name)

greet_user('Daniel')

print('***********************')

message='global'
#outer function
def outer():
    message='local'
    
    #inner function
    def inner():
        nonlocal message #declaring nonlocal var
        message='nonlocal'
        print('inner: ',message)
        #calling inner function
    inner()
        
    print('outer: ',message)
    
print('most outer: ',message)
outer()


print('***********************')

c=1

def add():
    global c
    c = c+2
    
    print(c)
    
add()
print('***********************')

def outer_fn():
    num=20
    
    def inner_fn():
        global num
        num=30
        
        #print('inner fn num : ',num)
    print('Before calling inner_fn: ',num)    
    inner_fn()
    print('after calling inner_fn: ',num)
    
outer_fn()
print('outside both fns: ',num)

#This is because we have used the global keyword in num to create a global variable inside the inner_function() function (local scope).

#So, if we make any changes inside the inner_function() function, the changes appear outside the local scope, i.e. outer_function().

print('***********************')



