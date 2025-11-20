import csv
print("Enter the filename")
fname =input()
fptr = open(fname,"r")
row_num = int(input("Enter the row :"))
rea = csv.reader(fptr)
next(rea)
for current_row,row in enumerate(rea,start=1):
    if current_row == row_num:
        print(" ".join(row))
        break
else:
    print("no match found")