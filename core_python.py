# str1 = input("Enter the string :")
# str2 = input("Enter the string2 :")
# if str1 > str2:
#     print("Str 1 is grater")
# elif str1 < str2:
#     print("str2 is grater")
# else:
#     print("str1 is eqal to st2")


# str1 = input("Enter a string :")
# i = 0
# newstr = " "
#
# while(i<= len(str1)-1):
#     ext = str1[i]
#     ascii = ord(ext)
#     if (ascii >= 65 and ascii <= 90):
#         newascii = ascii + 32
#         converchar = chr(newascii)
#         newstr = newstr + converchar
#     else:
#         newascii = ascii - 32
#         converchar = chr(newascii)
#         newstr = newstr + converchar
#     i = i + 1
# print(newstr)

# str1 = input("Enter a string :")
# str2 = str1.lower()
# str3 = str1.upper()
# str4 = str1.swapcase()
# print(str1)
# print(str2)
# print(str3)
# print(str4)

# st1 = "if you think you can or you can't, you are right"
# print(len(st1))
# print(st1.find("you"))
# print(st1.index("you"))
# str2 = "you"
# print(str2 in st1)
# print(st1.rfind("you"))
# print(st1.rindex("you"))
# print(st1.find("rakesh"))
# print(st1.index("rakesh"))

str1 = input("Enter a string :")
if str1.isalpha():
    print("string contains only characters")
elif str1.isdigit():
    print("string contains only numbers")
elif str1.isalnum():
    print("string contains both numbers and characters")
else:
    print("enter a valid string")