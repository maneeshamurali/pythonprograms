# que=[]
# size=int(input("enter the size"))
# front=0
# rear=-1
# n=0
# def enque():
#     global front,rear,size
#     if rear>=size:
#         print("queue is full")
#     else:
#         p=int(input("enter the elemt to add"))
#         que.insert(rear,p)
#         rear+=1
# def deque():
#     global front, rear, size
#     if rear==-1:
#         print("queue is empty")
#     else:
#         p=int(input("elemt to remove"))
#         que.remove(p)
#         front -= 1
#         rear += 1
# def display():
#     print(que)
# while n!= 1:
#     print("enter the operation to perform")
#     opt = int(input("press 1.enque 2. deque 3.display"))
#     if opt == 1:
#         enque()
#     elif opt == 2:
#         deque()
#     elif opt == 3:
#         display()
#     else:
#         print("invalid input")
#     n = int(input("do you want to continue press 1 to exit"))


a=int(input("enter first elemt"))
b=int(input("enter secnd elemt"))
c=a/b
print(c)
