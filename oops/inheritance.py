# class Person:
#     def walk(self):
#         print("walking")
#     def read(self):
#         print("reading")
# class Student(Person):
#     def exam(self):
#         print("exam writing")
# p=Person()
# p.walk()
# p.read()
# s=Student()
# s.exam()
# s.walk()
# s.read()

# class Person:
#     def working(self,a):
#         self.a=a
#         print("working for",self.a,"hr time")
#     def chatting(self,name):
#         self.name=name
#         print("chatting to",self.name)
# class Employee(Person):
#     def reasting(self,hr):
#         self.hr=hr
#         print("chatting for",self.hr,"hr time")
# p=Person()
# p.working(4)
# p.chatting("manee")
# e=Employee()
# e.working(4)
# e.chatting("maneesha")
# e.reasting(5)
# a=int(input("enter initial range"))
# b=int(input("enter final range"))
# r=5
# for i in range(a,b):
#     if i%2==0:
#         for k in range(r,0,-1):
#             for j in range(0,k):
#                 print(i,end=" ")
#             print("\r")
#     else:
#         for l in range(r):
#             for m in range(0,l+1):
#                 print(i,end=" ")
#             print("\r")

# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# print(list(set(lst)))


# def sumprime(min,max):
#     sum=0
#     for a in range(min,max):
#         if a>1:
#             for i in range(2,a):
#                 if a%i==0:
#                     break
#             else:
#                 sum=sum+a
#     return sum
# print(sumprime(1,10))