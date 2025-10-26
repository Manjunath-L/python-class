def reverse_num(n,rev=0):
    if n <= 0:
        return rev
    rem = n%10
    rev = (rev*10)+rem
    n = n//10
    return reverse_num(n,rev)

n = int(input("Enter a number :"))
rev = reverse_num(n)
print(f"The reverse number is : {rev}")
