import re
text = "Python is super super super easy"
regex = r"Python"
res1 = re.match(regex,text)
print(res1)

text = "Python is super super super easy"
regex = r"super"
res1 = re.search(regex,text)
print(res1)


text = "Python is super super super easy"
regex = r"super"
res1 = re.findall(regex,text)
print(res1)

text = "Python is super super super easy"
regex = r"."
res1 = re.findall(regex,text)
print(res1)

text = "Python is easy."
regex = r"\."
res1 = re.findall(regex,text)
print(res1)

text = "Python is * easy"
regex = r"\*"
res1 = re.findall(regex,text)
print(res1)
# error
# text = "Python is * easy"
# regex = r"\p"
# res1 = re.findall(regex,text)
# print(res1)