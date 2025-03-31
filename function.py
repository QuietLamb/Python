# ************* Paper code ****************
# def mile2km(mi):
#     for i in range(1,6):
#         result = i*mi
#         print(i,'miles = ',result,'km')
# mile2km(1.61)

# ************* Paper code ****************
# def cel2fah(cel):
#     for i in range(1,6):
#         result = cel*9/5+32
#         cel+=10
#         print(i*10,'degress Celsius = ',result,'degrees Fahrenheit')
# cel2fah(10)

# ************* Mission ****************

import string

src_str = string.ascii_uppercase
dst_str = src_str[3:] + src_str[:3]
print(src_str)
print(dst_str)

def cipher(a):
    result = src_str.index(a)
    return dst_str[result]
src = input("Enter text: ")
print("Encrypted sentence is: ",end="")
for ch in src:
    if ch in src_str:
        print(cipher(ch),end="")
    else:
        print(ch,end="")
print()