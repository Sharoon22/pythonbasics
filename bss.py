"""print("hello")
print('1')
print(1+3)
print("hello\nworld")
print("\thelooooo")
#print('world'+12)string and interger patoola
print('world'*12)
#print('world'+1.2)string and float aayond
print(1+12)
print('1'+'12')

#Arithmetic operation
#1 Addition
print(1+2)

#2 Substraction
print(1-2)

#3 Multiplication
print(3*2)

#4 Division (integer aaykkm)
print(3/2)
print(5/5)

#5 Floor division (uses //)
print(3//2)

#6 Modulo (remainder value use aakum)
print(3%2)
print(4%2)

#7 Exponential
print(2**5) #2^5

#8 Root
print(4**(1/2))

#Boolean Operators(<,>,!=,==,<=,>=)
print(2<3)
print(2>3)
print(2!=3)
print(2!=2)
print(2==2)
print(2==3)
print('Hello'=='Hello')#Comparison Operator By Checking Index of Both

#Variables(Used for temporary storage)
a=10
print(a)
print(a+30)
print(a*30)
b=20
print(a+b)# add a and b
print(id(a))#memory address of a
a=20 #memroy address change aavum ennit new edkkum ennit old garbage aavum
print(a)
c=5
d=8
e=c+d
print(e)
print("Result is",e)
e=c%d
print("Result is",e)
e=c**d #c^d (5^8)
print("Result is",e)


#Input Function
a=int(input('enter your 1st number:'))
b=int(input('enter your 2nd number:'))
c=a+b
d=a*b
print('result is',c,d)

#Type function
a=20
print(type(a))
c="hello"
print(type(c))



#Type conversion
print(int('2')+int('3'))
print(int(2.3)+int(4.5))
print(float(5)+float(7))

#swapping using third variable

a=10
b=5
print("Before swapping")
print("Value of a:",a)
print("Value of b:",b)
print("...............")
print("After swapping")
temp=a
a=b
print("value of a:",a)
b=temp
print("value of b:",b)
print("-----------")
a=5
b=10
print("Before swapping")
print("Value of a:",a)
print("Value of b:",b)
print("----------")
print("After swapping")

a,b =b,a
print("a=",a)
print("b=",b)"""


#Conditional statements

"""
1.if
2.ladder if
3.if else
4.ladder else if
5.elif
"""

#if condition
"""
if condition:
   statement"""

"""if 10>2:
    print("10 is greater")
print("program finished")"""

"""if 10-2==11-3:
    print("both are equal")
print("program finished")"""
"""print("-----------")
if 10-3==11-3:
    print("both are equal")
print("program finished")"""

#Ladder if

"""if condition:
    statement
    if condition:
        statement"""


"""if 10>2:
        print("10 is greater")
        if 10<2:
                print("2 is greater")"""

#else if
"""
    print("number is even")
if condition:
    statement
else:
    statement"""

"""a=int(input('enter your First number:'))
b=int(input('enter your Second number:'))
if a==b:
    print("square")
else:
    print("rectangle")

a=int(input('enter the number:'))
if a%2==0:
    print("number is even")
else:
    print("number is odd")"""
# if else ladder \\ eedelm 1 condition satisfy chydal ade edkllu

#syntax
"""
if condition:
    statement
else:
    if condition:
        statement
    else:
        statement"""
"""
a=10
if a==10:
    print("hello")
else:
    if a>2:
     print("hai")
    else:
        print("world")"""

# VOWEL OR NOT USING IN OPERATOR
"""
z=input('enter a character:')
vowel="aeiouAEIOU"
if z in vowel:
    print("it is vowel")
else:
    print("it is not vowel")"""

#PRINT RGB COLOR

"""color = input ('enter a color')
if color =="red":
    print('color is red')
else:
    if color == "blue":
        print('color is blue')
    else:
        if color == "green":
            print ('color is green')
        else:
            print ('its not RBG color code')"""
# Elif
"""color = input ('enter a color')
if color =="red":
    print ('color is red')
elif color == "blue":
    print ('color is blue')
elif color == "green":
    print ('color is green')
else:
    print ('its not RBG color code')"""

# and
"""
a=int(input('enter your 1st number:'))
b=int(input('enter your 2nd number:'))
c=int(input('enter your 3rd number:'))
if a>b and a>c :
    print(f"[a] is greater")
elif b>a and b>c :
    print(f"[b] is greater")
else:
    print(f"[c] is greater")"""

# LOOP

#1 While
#syntax
"""intialization
 while condition(limit):
     statement
     increment

i=1
while i<=10:
    print("hello")
    i+=1
print("finished")
"""
"""
a=1
while a<=10:
    print(a)
    a+=1"""
"""
a=2
while a<=10:
    if a%2==0:
        print(a)
    a+=2"""

#Break
"""while 1==1:
     print("hello")
     break"""

"""i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1"""

#continue
#1
'''i=0
while i<9:
    i+=1
    if i==5:
        continue
    print(i)'''
#2
"""i=0
while i<=10:
    i+=1
    if i==2:
        print("skipping 2")
        continue
    if i==5:
        print('hello')
        break
    print(i)"""

#3
'''i=10
while i>0:
    if i==5:
        i-=1
        break
    print(i)
    i-=1
print("hai")'''



#local and global
"""data='hello' """#global variable
"""def index():
    x=34""" #local variable
""" global y """# y ine global aaki
"""  y=100
    print('value of data:',data)
index()
print(data)
print('value of y is:',y)    
   """

#1 positional arguments
"""a=int(input('enter your num1:'))
b=int(input('enter your num2:'))
def addition(num1,num2):
    total=num1+num2
    print(total)
addition(a,b)"""

#2 keyword arguments
"""
def student(name,age,subject):
    print("name of student:",name)
    print("age of student:",age)
    print("subject of student:",subject)
student(subject="english",name="john",age=20)"""

#3 Default parameters
"""def multiply(a=10,b=10):
    print(a*b)
multiply(20,20)
multiply()"""
#
def multiply(a,b):
    print(a*b)
multiply(20,20)


    













    

    
    


        

        
    
    

              

