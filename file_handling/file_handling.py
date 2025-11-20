import csv
print("Enter the filename")
fname = input()
fptr = open(fname,"r")
rea = csv.reader(fptr)
next(rea)
for row in rea:
    print("Ename: ",row[2])