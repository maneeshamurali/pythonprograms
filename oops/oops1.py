# class Person:
#     def walk(self):
#         print("person is walking")
#     def read(self):
#         print("person is reading")
# p1=Person()
# p1.walk()
# p1.read()
#
# p2=Person()
# p2.walk()
# p2.read()

#
# class Book:
#     def read(self):
#         print("read the book")
#     def write(self):
#         print("write to book")
# b1=Book()
# b1.read()
# b1.write()



# class Person():
#     def setvalue(self,name,age):
#         self.name=name
#         self.age=age
#     def printvalue(self):
#         print("name",self.name)
#         print("age",self.age)
# p1=Person()
# p1.setvalue("manee",26)
# p1.printvalue()


# class Employee:
#     def setvalue(self,id,name,salary,age,cmpny_name,dept):
#         self.id=id
#         self.name=name
#         self.salary=salary
#         self.age=age
#         self.cmpny_name=cmpny_name
#         self.dept=dept
#     def printvalue(self):
#         print(self.id,self.name,self.salary,self.age,self.cmpny_name,self.dept)
#         # print("name",self.name)
#         # print("salary",self.salary)
#         # print("age",self.age)
#         # print("company name",self.cmpny_name)
#         # print("deppartment",self.dept)
# e1=Employee()
# e1.setvalue(1,"manee",30000,21,"ust","developer")
# e1.printvalue()

# class Add:
#     def getvalue(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def printvalue(self):
#         print(self.num1+self.num2)
# a=Add()
# num1=int(input("enter first num"))
# num2=int(input("enter secnd num"))
# a.getvalue(num1,num2)
# a.printvalue()


# class Student:
#     def setvalue(self,name,clas,schoolname,rollnumber):
#         self.name=name
#         self.clas=clas
#         self.schoolname=schoolname
#         self.rollnumber=rollnumber
#     def getvalue(self):
#         print("name", self.name,"clas", self.clas,"schoolname",self.schoolname,"rollnumber",self.rollnumber)
# s=Student()
# s.setvalue("manee",10,"sngce",8)
# s.getvalue()

# class Student:
#     school="luminar"
#     def setvalue(self,name,clas,rollnumber):
#         self.name=name
#         self.clas=clas
#         self.rollnumber=rollnumber
#     def getvalue(self):
#         print(self.name)
#         print(self.clas)
#         print(self.rollnumber)
#         print(Student.school)
# s=Student()
# s.setvalue("manee",10,8)
# s.getvalue()
# s1=Student()
# s1.setvalue("maneesha",10,8)
# s1.getvalue()


class Employee:
    companyname="luminar"
    def setvalue(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def getvalue(self):
        print(self.name)
        print(self.id)
        print(self.salary)
        print(Employee.companyname)
e=Employee()
e.setvalue("manee",10,80000)
e.getvalue()
e1=Employee()
e1.setvalue("maneesha",10,500000)
e1.getvalue()


