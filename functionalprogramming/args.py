# def printv(*args):
#     return args
# print(printv(3,6,8,9))
#
# def printv(*args):
#     return args
# print(printv("manee",45,9.0))


# def printv(**args):
#     return args
# print(printv(place="kochi",age=21,name="manee"))


def printv(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(printv(1,2,3,4,5,6))