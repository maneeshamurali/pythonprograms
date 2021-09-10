# def revert_val(func):
#     def wrapper(no1,no2):
#         if no1<no2:
#             (no1,no2)=(no2,no1)
#             return func(no1,no2)
#         else:
#             return func(no1,no2)
#     return wrapper
# @revert_val
# def div(num1,num2):
#     return num1/num2
# print(div(2,10))
# @revert_val
# def div(num1,num2):
#     return num1-num2
# print(div(1,10))


# def admin_required(func):
#     def wrapper(a,b):
#         if a!="admin":
#             raise Exception("you are not allowed")
#         else:
#             return func(a,b)
#     return wrapper
# @admin_required
# def change_pin(user,pin):
#     mypin=pin
#     return mypin
# @admin_required
# def delete_ac(user,aco):
#     return str(aco)+"deleted"
# print(change_pin("admin",1000))
# print(delete_ac("admin",1000))

def vaccine(func):
    def wrapper(a,b,c):
        if b<18:
            raise Exception("not applicable")
        else:
            return func(a,b,c)
    return wrapper
@vaccine
def vaccine_det(name,age,place):
    return "sucessfully registered"
print(vaccine_det("manee",19,"vgra"))