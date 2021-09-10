# a=int(input("enter first elemt"))
# b=int(input("enter secnd elemt"))
# c=a/b
# print(c)

# a=int(input("enter first elemt"))
# b=int(input("enter secnd elemt"))
# try:
#     res=a/b
#     print(res)
# except:
#     print("error occured")

# lst=[0,7,8]
# n=int(input("enter the index to find elemt"))
# try:
#     print(lst[n])
# except:
#     print("error")


# a=[0,7,8]
# n=int(input("enter the index to find elemt"))
# try:
#     print(a[n])
# except:
#     print("error")
# finally:
#     print("index out of bound")


# lst=[0,7,8]
# n=int(input("enter the index to find elemt"))
# try:
#     print(lst[n])
# except Exception as e:
#     print(e.args)
# finally:
#     print("completed")

# a=int(input("enter first elemt"))
# b=int(input("enter secnd elemt"))
# try:
#     res=a/b
#     print(res)
# except Exception as e:
#     print(e.args)
# finally:
#     print("completed")


# a=int(input("enter num1"))
# b=int(input("enter num1"))
# if b>a:
#     raise Exception("num2 is greater")
# else:
#     print(a/b)

age=int(input("enter the age"))
if age<18:
    raise Exception("age mismatch error")
else:
    print("eligible")
