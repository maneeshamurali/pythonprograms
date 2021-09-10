# def linear(n):
#     lst=[1,2,3,4,5,6,7,8,9,99,88,77,66,55,44,22,11]
#     fla=0
#     for i in lst:
#         if(i==n):
#             fla=1
#     if fla==1:
#         print("present")
#     else:
#         print("not present")
# linear(45)


# lst=[1,2,3,4]
# a=0
# for i in lst:
#     a+=i
# print(a)

# a=[]
# n=int(input("enter the size"))
# for i in range(n):
#     e=int(input("enter the element"))
#     a.append(e)
# b = 0
# for i in a:
#     b += i
# print(b)

# lst=[1,2,3,4,5,6]
# print(lst[0])
# print(lst[-1])
# print(lst[4])
#
# lst=[9,1,3,7,3,4,0,5]
# sort=[]
# min=lst[0]
# max=lst[-1]
# for i in lst:
#     if lst[i]>lst[i+1]:
#         sort[i]=list[i]
#         lst[i]=lst[i+1]
#         lst[i+1]=sort[i]
#     else:
#         continue
# print(lst)

# lst=[1,2,3,4,5,6,7]
# print(lst[1:3])
# print(lst[-4:-1])
# print(lst[:4])
# print(lst[3:])
# print(lst[:])
# print(lst[1:6:2])
#
# lst=[1,2,3,4,1,2]
# b=[]
# for i in lst:
#     if i not in b:
#         b.append(i)
#     else:
#         print(i)

# lst=[2,3,5,1,6,-1,8,7,9,11,0]
# min=lst[0]
# max=lst[-1]
# for i in lst:
#     if i<min:
#         min=i
# # for j in lst:
#     if i>max:
#         max=i
# print("min=",min)
# print("max=",max)

# lst=[1,2,3,5,6,4,8,9]
# b=[]
# for i in lst:
#     b.append(i*5)
# print(b)

# ls=[1,2,3,4,5,6,7,8,9,10]
# a=[i for i in ls if i%2==0]
# print(a)
# b=[i for i in ls if i%2!=0]
# print(b)

# s=[a for a in range(100,200) if a%2==0]
# print(s)

a=[1,2,3,4]
s=1
for i in a:
    s*=i
print(s)
