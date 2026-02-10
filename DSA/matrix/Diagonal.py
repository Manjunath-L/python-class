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

def printSqureMat(arr):
    for i in range(0,len(arr)):
        print(arr[i],end="\n")
        

def checkDiagonals(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if not((i==j) or (i+j == len(arr) - 1)):
                arr[i][j] = 0
                

arr = createSquareMatrix()
print("Original matrix")
printSqureMat(arr)
checkDiagonals(arr)
print("NON-Diagonals elements")
printSqureMat(arr)
    