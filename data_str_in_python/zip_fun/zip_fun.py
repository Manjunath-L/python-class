from itertools import zip_longest

names = ["virat","rohit","gill","rajath"]
ipl_t = ["RCB","MI","GT","RCB"]
ipl_r = [8000,7000,6000,5000]
country = ["IND","IND"]

info = list(zip(names,ipl_t,ipl_r,country))
print(info)

info = list(zip_longest(names,ipl_t,ipl_r,country,fillvalue="#"))
print(info)