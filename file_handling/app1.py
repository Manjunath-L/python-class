# print("Enter the filename")
# fname=input()
# fptr=open(fname,"r")
# data1=fptr.read()
# print(data1)

# print("Enter the filename")
# fname=input()
# fptr=open(fname,"r")
# data2=fptr.read(15)
# print(data2)

# print("Enter the filename")
# fname=input()
# fptr=open(fname,"r")
# data1=fptr.readline()
# data2=fptr.readline()
# print(data1)
# print(data2)


# print("Enter the filename")
# fname=input()
# fptr=open(fname,"r")
# data2=fptr.readlines()
# print(data2)

#split()method:
# str1="Rama is eating"
# print(len(str1))
# str2=str1.split()
# print(len((str2)))
# print(str2)

fptr=open("emp.txt","r")
print("Filename:",fptr.name)
print("Filemode:",fptr.mode)
print("writable:",fptr.writable)
print("readable:",fptr.readable)
print("colsed:",fptr.closed)
fptr.close()
print("colsed:",fptr.closed)