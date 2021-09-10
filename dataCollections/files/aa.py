# f1=open('filedemo1','r')
# for i in f1:
#     print(i)

# f=open('filedemo1','w')
# f.write("hello maneesha")
# f.write("\nhow are you?")

# f=open('filedemo1','r')
# f1=open('filenew','w')
# for i in f:
#     f1.write(i)



def push(x):
    return x
def pop(x):
    return x
def display(x):
    return x

print("1.push")
print("2.pop")
print("3.display")
n=int(input("enter the size"))
while True:
    lst = []
    ch=int(input("enter the choice"))

    if ch==1:
        if len(lst)==n:
            break
        else:
            y = int(input("enter the number to add"))
            lst.append(y)
    elif ch==2:
        y = int(input("enter the number to remove"))
        lst.remove()
    elif ch==3:
        print(lst)

# a=int(input("enter initial range"))
# b=int(input("enter final range"))
# for i in range(a,b):
#     if i%2==0:
#         for i in range(b,0,-1):
#             for j in range(0,i):
#                 print(i,end=" ")
#             print("\r")
#     else:
#         for i in range(b):
#             for j in range(0,i):
#                 print(i,end=" ")
#             print("\r")


# s=[a for a in range(1,100) if a%5==0]
# print(s)
#  it is an easy and compact syntax for creating a list.
# It is a very concise way to create a new list by performing an operation on each item in the existing list.
# it reduces the code.using  one or two lines we can perform that.




# Reducing duplication of code.
# Decomposing complex problems into simpler pieces.
# Improving clarity of the code.
# Reuse of code.



# s=input("enter the string")
# vowels='a','e','i','o','u','A','E','I','O','U'
# novowels=""
# for char in s:
#     if char not in vowels:
#         novowels=novowels+char
# print(novowels)


# l=int(input("enter lower limit"))
# u=int(input("enter upper limit"))
# def sum(l,u):
#     s=0
#     for num in range(2,u+ 1):
#         i = 2
#         for i in range(2, num):
#             if (int(num % i) == 0):
#                 i = num
#                 break;
#         if i is not num:
#             s += num
#             return s
# print(sum(l,u))

#
# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     return x/y
# def floordiv(x,y):
#     return x//y
# def exp(x,y):
#     return x**y
# print("1.add")
# print("2.substraction")
# print("3.multiply")
# print("4.division")
# print("5.floor division")
# print("6.exponent")
#
# while True:
#     choice=int(input("enter the choice"))
#     n1 = int(input("enter the first number"))
#     n2 = int(input("enter the second number"))
#     if choice==1:
#         print("result is",add(n1,n2))
#     elif choice==2:
#         print("result is", sub(n1,n2))
#     elif choice==3:
#             print("result is",mul(n1,n2))
#     elif choice==4:
#             print("result is",div(n1,n2))
#     elif choice==5:
#             print("result is",floordiv(n1,n2))
#     elif choice==6:
#             print("result is",exp(n1,n2))
#     else:
#         print("enter valid choice")
#
#
#
# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# newlst=[]
# for i in lst:
#     if i not in newlst:
#         newlst.append(i)
# print(newlst)
#
# lst=[s.append(i) for i in lst if i not in s ]
#
# lst=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# lst.sort()
# print(lst[-2])
#
#
# a=[1,2,3,45,6,7,33,11,77,9,0,5]
# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
# for i in a:
#     for j in b:
#         if i==j:
#             print(i)


# lst=["abc",1,2,3]
# lst1=[6,3,4]
# # lst.extend(lst1)
# lst.append(lst1)
# print(lst)