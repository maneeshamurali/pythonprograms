employees = [
    {"e_id": 1000, "e_name": "ram", "salary": 25000, "department": "testing", "exp": 1},
    {"e_id": 1001, "e_name": "ravi", "salary": 22000, "department": "ba", "exp": 1},
    {"e_id": 1002, "e_name": "raj", "salary": 20000, "department": "mrkt", "exp": 1},
    {"e_id": 1003, "e_name": "nikil", "salary": 26000, "department": "developer", "exp": 1},
    {"e_id": 1004, "e_name": "nivi", "salary": 28000, "department": "developer", "exp": 2},

]
# for employee in employees:
#     print(employee["e_name"])
# e_names=list(map(lambda employee:employee["e_name"],employees))
# print(e_names)
# e_upper=list(map(lambda emp:emp["e_name"].upper(),employees))
# print(e_upper)



# for employee in employees:
#     print(employee["e_name"].upper())


# for employee in employees:
#     if(employee["department"]=="developer"):
#         print(employee["e_name"])
# dev=list(filter(lambda emp:emp["department"]=="developer",employees))
# print(dev)
# dev_name=list(map(lambda developer:developer["e_name"],list(filter(lambda emp:emp["department"]=="developer",employees))))
# print((dev_name))



#
# total=0
# for employee in employees:
#     total=+employee["salary"]
# print(total)
#




# lst=[2,3,4,5,6]
# map
# cubes=list(map(lambda num:num**3,lst))
# print(cubes)
# square=list(map(lambda num:num**2,lst))
# print(square)


# filter
# even=list(filter(lambda num:num%2==0,lst))
# print(even)
# odd=list(filter(lambda num:num%2!=0,lst))
# print(odd)


num=int(input("enter num"))
print("+ve" if num>0 else "-ve" )