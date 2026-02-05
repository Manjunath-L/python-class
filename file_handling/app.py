print("Enter the fie name")
fname=input()

with open(fname,"a") as fptr:
    for i in range (5):
        eid=input("Enter the eid")
        ename=input("Enter the ename")
        edes=input("Enter the edes")
        esal=input("Enter the esal")
        eadd=input("Enter the eadd")
    fptr.write(eid+"\t"+ename+"\t"+edes+"\t"+esal+"\t"+eadd+"\n")
print("5 emp details are stored")