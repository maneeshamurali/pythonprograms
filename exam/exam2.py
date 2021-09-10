# class vehicle:
#     def run(self):
#         print("vehicle is running")
#     def stop(self):
#         print("vehicle is stopped")
# class Bus(vehicle):
#     def breaking(self):
#         print("bus is breaking")
# b=Bus()
# b.run()
# b.stop()
# b.breaking()


# class Person:
#     def set(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class employee:
#     def seeet(self,hrs):
#         self.hrs=hrs
#         print(self.hrs)
# class Child(Person):
#     def setv(self,name,age,school):
#         self.name=name
#         self.age=age
#         self.school=school
#         print(self.name,self.age,self.school)
# class Parent(Person,employee):
#     def prnt(self,name,salary):
#         self.name=name
#         self.salary=salary
#         print(self.name,self.salary)
# class Student(Child):
#     def prn(self,std,id):
#         self.std=std
#         self.id=id
#         print(self.std,self.id)
# p=Person()
# p.set("manee",21)
# c=Child()
# c.setv("anu",14,"abc")
# c.set("ammu",24)
# pa=Parent()
# pa.prnt("naa",25000)
# pa.set("maa",25)
# pa.seeet(5)
# s=Student()
# s.prn(7,123)
# s.setv("kaa",12,"gcd")


# class Book:
#     library_name="abc"
#     def __init__(self,book_name,author,pages):
#         self.book_name=book_name
#         self.author=author
#         self.pages=pages
#     def printv(self):
#         print(self.book_name)
#         print(self.author)
#         print(self.pages)
#         print(Book.library_name)
# b=Book("gorilla","ebcc",157)
# b.printv()
#
# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printv(self):
#         print(self.name)
#         print(self.age)
# class Dog(Animal):
#     def __init__(self,name,color):
#         super.__init__(name,age)
#         self.name=name
#         self.color=color
#     def printval(self):
#         print(self.name)
#         print(self.color)
# d=Dog("roobi","black")
# d.printval()
#
#
# method overriding is the same method name and same number of arguments
# eg:
# class Book:
#     def printval(self,name):
#         self.name=name
#         print(self.name)
# class page(Book):
#     def printval(self,school):
#         self.class1=school
#         print(self.school)
# c=Book()
# c.printval("abc")






# import re
# f1=open("phn_num",'r')
# f2=open("phn_numm",'w')
# x='[+][9][1]\d{10}$'
# for num in f1:
#     number=num.rstrip("\n")
#     matcher=re.fullmatch(x,number)
#     if matcher !=None:
#         f2.write(num)






# finally block executed when the exception occures.finally block execute. if an exception occurs first run try block
# if try block rise exception then except block will run. finally block run whether the try or except runs.
#
#     eg:
# a=[1,2,3]
# index=int(input("enter the index"))
# try:
#     print(a[index])
# except:
#     print("not exist")
# finally:
#     print("index finally")







# import re
# x='[A-Z]+[a-zA-Z0-9]{3,8}[A-Z]$'
# n=input("enter string")
# matcher=re.fullmatch(x,n)
# if matcher!=None:
#     print("valid")
# else:
#     print("invalid")
#



# import re
# n=input("enter the string")
# x='^[A-Z][a-z]*$'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
# #




#
# import re
# n=input("enter the mob num to validate")
# x='^a[0-9]*b$'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
#
#
# #
# The __str__ method in Python represents the class objects as a string – it can be used for classes.
# The __str__ method should be defined in a way that is easy to read and outputs all the members of the class.
#
# eg:

# class vehicle:
#     def __init__(self,model,regno):
#         self.model=model
#         self.regno=regno
#     def printv(self):
#         print(self.model,self.regno)
#     def __str__(self):
#         return self.model
#
# v=vehicle("ktm","12345")
# v.printv()
# print(v)






# class Student:
#     def __init__(self,name,rollno,dept,clg):
#         self.name=name
#         self.rollno=rollno
#         self.dept=dept
#         self.clg=clg
#     def printv(self):
#         print("name",self.name)
#         print("rollno",self.rollno)
#         print("dept",self.dept)
#         print("clg",self.clg)
#     def __str__(self):
#         return self.name+str(self.rollno)
# s=Student("manee",123,"cse","luminar")
# s.printv()
# print(s)
#






a=lambda x:x%2==0
print(a(5))






# class Student:
#     def __init__(self,name,rollno,course,mark):
#         self.name=name
#         self.rollno=rollno
#         self.course=course
#         self.mark=mark
#     def printdata(self):
#         print(self.name)
#         print(self.rollno)
#         print(self.course)
#         print(self.mark)
# lst=[]
# f=open("wrkk","r")
# for i in f:
#     d=i.rstrip("\n").split(",")
#     print(d)
#     name=d[0]
#     rollno=d[1]
#     course=d[2]
#     mark=d[3]
#     s1=Student(name,rollno,course,mark)
#     s1.printdata()
#     lst.append(s1)
# mark=[]
# for st in lst:
#     mark.append(st.mark)
# print(mark)
# for st in lst:
#     if (st.mark==max(mark)):
#         print(st.rollno,st.name,st.course,st.mark)