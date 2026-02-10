#deafult square matrix
from Lib.test.test_warnings.data.stacklevel import inner


def createDeafultSquareMatrix():
    outer = []
    n = int(input("Enter size :"))
    for i in range(0,n):
        inner = [0]*n
        outer.append(inner)

    return outer

#Dynamic Valued Square Matrix
def createSquareMatrix():
    outer = []
    n = int(input("Enter a size :"))
    #rows
    for i in range(0,n):
        inner = []
        for j in range(0,n):
            inner.append(int(input("Enter a value :")))
        outer.append(inner)
    return outer

#deafult rectangul Matrix
def createDeaRectMat():
    outer = []
    n = int(input("Enter num of rows :"))
    m = int(input("Enter num of cols :"))
    for i in range(0,n):
        inner = [0] * m
        outer.append(inner)
    return outer

#dynamic rectangungler matrix
def createDynRectMat():
    outer = []
    n = int(input("Enter num of rows :"))
    m = int(input("Enter num of cols :"))
    for i in range(0,n):
        inner = []
        for j in range(0,m):
            inner.append(int(input("Enter a value: ")))
        outer.append(inner)
    return outer

# arr = createDeafultSquareMatrix()
# print(arr)
# arr1 = createSquareMatrix()
# for i in range(0 , len(arr1)):
#     print(arr1[i])
#
# arr = createDeaRectMat()
# print(arr)
arr = createDynRectMat()
for i in range(0,len(arr)):
    print(arr[i],end="\n")
