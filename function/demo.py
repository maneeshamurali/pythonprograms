# function without argument
# def add():
#     num1=int(input("enter the first num"))
#     num2=int(input("enter the second num"))
#     res=num1+num2
#     print("result is",res)
# add()

# function without argument
#
# def add(num1,num2):
#     print(num1+num2)
# add(13,25)

# function with arguments and return type
# def add(num1,num2):
#     return num1+num2
# print(add(10,20))

# prgm to check a number is odd or even
# def num():
#     n=int(input("enter the number"))
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# num()
# num()
#
# factorial using function with arguments
# def fact(n):
#     factorial=1
#     if n>0:
#         for i in range(1,n+1):
#             factorial=factorial*i
#         print(factorial)
#     elif n==0:
#         print("factorial is 1")
#     else:
#         print("enter a positive number")
# fact(5)


#sum of n numbers
# def sum(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     return(sum)
# print(sum(5))
# for creating infinite loop
# while False:
#     print("hello")

# calculator program
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def floordiv(x,y):
    return x//y
def exp(x,y):
    return x**y
print("1.add")
print("2.substraction")
print("3.multiply")
print("4.division")
print("5.floor division")
print("6.exponent")

while True:
    choice=int(input("enter the choice"))
    n1 = int(input("enter the first number"))
    n2 = int(input("enter the second number"))
    if choice==1:
        print("result is",add(n1,n2))
    elif choice==2:
        print("result is", sub(n1,n2))
    elif choice==3:
            print("result is",mul(n1,n2))
    elif choice==4:
            print("result is",div(n1,n2))
    elif choice==5:
            print("result is",floordiv(n1,n2))
    elif choice==6:
            print("result is",exp(n1,n2))
    else:
        print("enter valid choice")

# fibonacci program
# n=int(input("enter the number"))
# t1=0
# t2=1
# for i in range(1,n+1):
#     print(t1)
#     next=t1+t2
#     t1=t2
#     t2=next
# prime numbers

# n=int(input("enter the number"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("not a prime number")
#             break
#         else:
#             print("it is a prime number")
#             break
# else:
#     print("enter positive number")
# another method
# n=int(input("enter the number"))
# fla=0
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         fla=1
# if fla==1:
#     print("prime")
# else:
#     print("not prime")

# prime number between range
#

# a="abcd"
# b="acfg"
# for i in a:
#     for j in b:
#         if i==j:
#             print(i)
#         else:
#             continue

# a="luminar"
# b=input("enter an element")
# for i in a:
#     if i==b:
#         print("present")
#         break
# else:
#     print("not present")
# a="malayalam"
# b=input("enter element to be count")
# count=0
# for i in a:
#     if i==b:
#         count=count+1
#         continue
# print(count)
# else:
# print("not present")
# a=input("enter the string")
# b=""
# for i in a:
#     if i=='='&& i==';'&& i==':':
#         continue
#         b=b+i
# for i in range(5,0,-1):
#     for j in range(0,i-1):
#         print("*",end=" ")
#     print("\r")







