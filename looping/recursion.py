# def fact(x):
#     if x==0:
#         return 1
#     else:
#         return x * fact(x-1)
# num=int(input("enter thew number"))
# print("factorial is ",fact(num))

# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# nterms=10
# for i in range(nterms):
#     print(fib(i),end=" ")

marks=int(input("enter the marks"))
if marks>=90:
    print("A PLUS")
elif 80<=marks<90:
    print("A")
elif 70<=marks<80:
    print("B plus")
elif 60<=marks<70:
    print("B")
elif 50<=marks<60:
    print("c ")
else:
    print("failed")