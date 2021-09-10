# class A:
#     def printa(self):
#         print("inside A")
# class B(A):
#     def printb(self):
#         print("inside b")
# class C(B):
#     def printc(self):
#         print("inside c")
# a=A()
# a.printa()
# b=B()
# b.printb()
# b.printa()
# c=C()
# c.printc()
# c.printb()
# c.printa()


# class Person:
#     def set(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class Child(Person):
#     def setv(self,name,age,school):
#         self.name=name
#         self.age=age
#         self.school=school
#         print(self.name,self.age,self.school)
# class Student(Child):
#     def prn(self,std,id):
#         self.std=std
#         self.id=id
#         print(self.std,self.id)
# p=Person()
# p.set("manee",21)
# c=Child()
# c.setv("anu",14,"abc")
# c.set("manee",21)
# s=Student()
# s.prn(7,123)
# s.setv("maneesha",21,"luminar")
# s.set("manee",21)


# class Person:
#     def set(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class Child(Person):
#     def setv(self,name,age,school):
#         self.name=name
#         self.age=age
#         self.school=school
#         print(self.name,self.age,self.school)
# class Parent(Person):
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
# c.setv("maneesha",14,"abc")
# c.set("manee",21)
# pa=Parent()
# pa.prnt("name",25000)
# pa.set("maaa",25)
# s=Student()
# s.prn(7,123)
# s.setv("kaaa",12,"gcd")

#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printval(self):
#         print("name",self.name)
#         print("age",self.age)
# class Student(Person):
#     def __init__(self,rollno,mark,name,age):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.mark=mark
#     def print(self):
#         print("rollno",self.rollno)
#         print("mark",self.mark)
# c=Student(2,34,"manee",21)
# c.printval()
# c.print()


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printval(self):
#         print("name",self.name)
#         print("age",self.age)
# class Employee(Person):
#     def __init__(self,dept,salary,name,age):
#         super().__init__(name,age)
#         self.dept=dept
#         self.salary=salary
#     def print(self):
#         print("dept",self.dept)
#         print("salary",self.salary)
# e=Employee("cse",25000,"manee",21)
# e.printval()
# e.print()

# class Vehicle:
#     def __init__(self,model,regno,color):
#         self.model=model
#         self.regno=regno
#         self.color=color
#     def printval(self):
#         print("model",self.model)
#         print("regno",self.regno)
#         print("color",self.color)
#     def __str__(self):
#         return self.model
# v=Vehicle("ktm","kl08 681","white")
# v.printval()
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

class Parent:
    def __init__(self,name,adrs,age):
        self.name=name
        self.adrs=adrs
        self.age=age
    def printv(self):
        print(self.name)
        print(self.adrs)
        print(self.age)
class Teacher(Parent):
    def __init__(self,dept,salary,id,name,adrs,age):
        super().__init__(name,adrs,age)
        self.dept=dept
        self.salary=salary
        self.id=id
    def setval(self):
        print(self.dept)
        print(self.salary)
        print(self.id)
    def __str__(self):
        return self.name+str(self.id)
t=Teacher("cse",35000,123,"manee","kzhm",21)

t.setval()
print(t)