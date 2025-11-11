a = "abc123def456"
b = []
# for data in  a:
#     if (data.isdigit()):
#         b.append(data)
# print(b)
# b = [data for data in a if data.isdigit()]
# print(b)

for data in  a:
    if (data.isalpha()):
        b.append(data)
print(b)
b = [data for data in a if data.isalpha()]
print(b)