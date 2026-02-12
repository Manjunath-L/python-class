# WAP to collect the information of the employee and store each employee information in a single line .csv file
# CSV[Comma Separated Values]:
import csv
print("Enter the filename:")
fname = input()
fptr = open(fname, "w", newline="")
w = csv.writer(fptr)
w.writerow(["EID","ENAME","EDES","ESAL","EADDR"])
for i in range(5):
    eid = input("Enter the eid: ")
    ename = input("Enter the ename: ")
    edes = input("Enter the edesignation: ")
    esal = input("Enter the esalary: ")
    eaddr = input("Enter the eaddress: ")
    w.writerow([eid, ename, edes, esal, eaddr])
fptr.close()
print("employee details are stored in csv file")