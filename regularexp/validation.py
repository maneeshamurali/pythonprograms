# import re
# n="56kg"
# x='[0-9]{2}[k][g]'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# import re
# n=input("enter the mob num to validate")
# x='\d{10}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# import re
# n=input("enter the mob num to validate")
# x='[+][9][1]\d{10}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


# import re
# n=input("enter the registration num")
# x='[K][L]\d{2}[A-Z]{2}\d{4}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

import re
n=input("enter the string")
x='[a-zA-Z]+\d{1}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")