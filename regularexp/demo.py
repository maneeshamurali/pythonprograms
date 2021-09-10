# import re
# count=0
# matcher=re.finditer('ab','ababaab')
# for match in matcher:
#     count+=1
# print("count=",count)
#
# import re
# count=0
# matcher=re.finditer('ab','ababaab')
# for match in matcher:
#     print("match available at",match.start())
#     print("group by",match.group())
#     count+=1
# print("count=",count)

# x='[abc]' either a b or c
# x='[^abc]' except abc
# x='[a-z]' a to z
# x='[A-Z]'   A to Z
# x='[a-zA-Z]' both lower and highr case are checked
# x='[0-9]' check digits
# x='[a-zA-Z0-9]' special symbols
# x='\s' check space
# x='\d' check the digits
# x='\D' except digits
# x='\w' all words except special characters
# x='\W' for special characterS

# import re
# x='[abc]'
# matcher=re.finditer(x,'abc resabgc')
# for match in matcher:
#     print("match available at",match.start())
#     print("group by",match.group())

# import re
# x='[^abc]'
# matcher=re.finditer(x,'abc resabgc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='[a-z]'
# matcher=re.finditer(x,'@ABas10')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='[A-Z]'
# matcher=re.finditer(x,'@ABas10')
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x='[a-zA-Z]'
# matcher=re.finditer(x,'@ABas10')
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x='[0-9]'
# matcher=re.finditer(x,'@ABas10')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='[^a-zA-Z0-9]'
# matcher=re.finditer(x,'@ABa s10')
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x='\w'
# matcher=re.finditer(x,'@ABas10')
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x='\W'
# matcher=re.finditer(x,'@ABa !s10')
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x='\d'
# matcher=re.finditer(x,'@ABas10')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='\D'
# matcher=re.finditer(x,'@ABas10')
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# import re
# x='\s'
# matcher=re.finditer(x,'@A Ba s10')
# for match in matcher:
#     print(match.start())
#     print(match.group())

#
# quantifiers
#
# x='a+'  a including group
# x='a*'  count including zero number of a
# x='a?' count a as each including zero no of a
# x='a{2}' 2 no of a position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a'  check starting with a
# x='a$' check ending with a

# import re
# x='a+'
# matcher=re.finditer(x,'aaa caga aaaaa ')
# for match in matcher:
#     print(match.start())
#     print(match.group())
# import re
# x='a*'
# matcher=re.finditer(x,'aa gcs abc')
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x='a?'
# matcher=re.finditer(x,'aa gcs abc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='a{2}'
# matcher=re.finditer(x,'aa gcsaa aaaaa abc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='a{1,3}'
# matcher=re.finditer(x,'aa aaaa agcs aabc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='^a'
# matcher=re.finditer(x,'aa gcs abc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='a$'
# matcher=re.finditer(x,'aa gcs abca')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# # f1=open("phn_num",'r')
# # x='[+][9][1]\d{10}$'
# # for num in f1:
# #     number=num.rstrip("\n")
# #     matcher=re.fullmatch(x,number)
# #     if matcher !=None:
# #         print(num)

