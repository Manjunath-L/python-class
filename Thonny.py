def findDigits(n):
    # Write your code here
    if n < 0:
        return n
    temp = n
    count = 0
    while n > 0:
        div  = n % 10
        if n != 0:
            if temp % div == 0:
                count = count + 1
        n = n // 10
    return count
    
findDigits(1012)