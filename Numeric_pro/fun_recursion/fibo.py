# def print_fibo(pos,n1,n2):
#     if pos <= 0:
#         return
#     print(n1,end=" ")
#     print_fibo((pos-1),n2,(n1+n2))
    
# num = int(input("Enter a number :"))
# print_fibo(num,0,1)

def fibo(pos):
    if pos == 0 or pos == 1:
        return pos
    return fibo(pos - 1) + fibo(pos - 2)

pos = int(input("Enter a number :"))
print(fibo(pos))