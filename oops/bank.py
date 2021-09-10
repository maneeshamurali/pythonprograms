# class Bank:
#     fixedamount=50000
#     def creation(self,mailid,password,amountdeposit):
#         self.mailid=mailid
#         self.password=password
#         print("account created")
#         self.amountdeposit=amountdeposit
#     def deposit(self,amounttodeposit,balance):
#         self.amounttodeposit=amounttodeposit
#         self.balance=balance
#         balanace=Bank.fixedamount+amounttodeposit
#         print("updated amount is",balance)
#
#     def widraw(self,amounttowidraw,balance):
#         self.amounttowidraw=amounttowidraw
#         self.balance=balance
#         balance=Bank.fixedamount-amounttowidraw
#         print("remaining amount",balance)
# b=Bank()
# b.creation("manee@123",123,50000)
#
#
# constructor


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printvalue(self):
#         print(self.name,self.age)
# p=Person("manee",21)
# p.printvalue()


# class Employee:
#     def __init__(self,name,id,salary):
#         self.name=name
#         self.id=id
#         self.salary=salary
#     def printvalue(self):
#         print(self.name,self.id,self.salary)
# e=Employee("manee",21,50000)
# e.printvalue()

# calculator

# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def add(self):
#         return self.num1+self.num2
#     def sub(self):
#         return self.num1-num2
#     def div(self):
#         return self.num1/self.num2
#     def mul(self):
#         return  self.num1*self.num2
# num1=int(input("enter"))
# num2=int(input(("enter")))
# c=Calculator(num1,num2)
# print(c.add())
# print(c.sub())
# print(c.div())
# print(c.mul())

class Teacher:
    cname="luminar"
    def __init__(self,tname,sub,dept,id):
        self.tname=tname
        self.sub=sub
        self.dept=dept
        self.id=id
    def printvalue(self):
        print(self.tname)
        print(self.sub)
        print(self.dept)
        print(self.id)
        print(Teacher.cname)
t=Teacher("ANU","maths","cse",123)
t.printvalue()