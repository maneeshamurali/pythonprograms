lst=[1,3,5,6,7,8,9,4]
def bsearch():
    lst.sort()
    print(lst)
    ele=int(input("enter elemnt to search"))
    fla=0
    low=0
    upp=len(lst)-1
    while low<=upp:
        mid=(low+upp)//2
        if ele>lst[mid]:
            low=mid+1
        elif low<lst[mid]:
            upp=mid-1
        elif ele==lst[mid]:
            fla=1
            break
    if fla==1:
        print("found")
    else:
        print("not found")

bsearch()