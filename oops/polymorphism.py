#
# overloading
# class Person:
#     def show(self,num1):
#         self.num1=num1
#         print(self.num1)
# class Student(Person):
#     def show(self,num2,num3):
#         self.num2=num2
#         self.num3=num3
#         print(self.num2,self.num3)
# s=Student()
# s.show(3)

# class Teacher:
#     def chat(self,name):
#         self.name=name
#         print(self.name)
# class Student(Teacher):
#     def chat(self,name1,name2):
#         self.name1=name1
#         self.name2=name2
#         print(self.name1,self.name2)
# s=Student()
# s.chat("manee","maneesha")
# s.chat("manee")


# class Operator:
#     def num(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(self.n1,self.n2)
#     def num(self,n1):
#         self.n1=n1
#         print(self.n1)
# o=Operator()
# o.num(6)
# o.num(4,6)

# overriding
#
# class Person:
#     def printval(self,name):
#         self.name=name
#         print("inside",self.name)
# class Child(Person):
#     def printval(self,class1):
#         self.class1=class1
#         print("outside",self.class1)
# c=Child()
# c.printval("manee")

# class Operator:
#     def add(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print(self.num1+self.num2)
#     def add(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#         print(self.num1 - self.num2)
# o=Operator()
# o.add(5,3)


# class Student:
#     def show1(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# f=open('filenew','r')
# for line in f:
#     l=line.split(",")
#     name=l[0]
#     age=l[1]
#     s=Student(name,age)
#     print(s)
#     s.show1()

#
# class Student:
#     def __init__(self,name,rolno,course,mark):
#         self.name=name
#         self.rolno=rolno
#         self.course=course
#         self.mark=mark
#     def printv(self):
#         print("name:",self.name)
#         print("rolno:",self.rolno)
#         print("course:",self.course)
#         print("mark:",self.mark)
#     def __str__(self):
#         return self.name
# f1=open("wrk","r")
# for line in f1:
#     l=line.split(",")
#     name=l[0]
#     rolno=l[1]
#     course=l[2]
#     mark=l[3]
#     st=Student(name,rolno,course,mark)
#     print(st)
#     st.printv()

count={}
f=open("wrk","r")
for n in f:
    wr=n.split(" ")
    for word in wr:
        if word not in count:
            count.update({word:1})
        else:
            val=int(count[word])
            val+=1
            count.update({word:val})
print(count)