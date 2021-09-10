# a=1,2,3,0,9
# print(a)
# a.remove(1)
# print(a)
# a.clear()
# print(a)

# a=2,
# print(a)

# tup=3,4.6,"dog"
# print(tup)
# a,b,c=tup
# print(a)
# print(b)
# print(c)

# tup=1,2,3,4
# a,b,c,d,=tup
# sum=a+b+c+d
# print(sum)

lst=[(1,"anu",28,20000),(2,"vinu",23,15000),(3,"ram",25,10000),(4,"ram",26,50000)]
for i in lst:
    if i[-1]>=15000:
        print(i)
