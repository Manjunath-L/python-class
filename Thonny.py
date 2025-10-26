def isSameAfterReversals(self, n: int) -> bool:
    if n <= 0:
        return True


    def rev_num(n, rev=0):
        if n <= 0:
            return rev
        rem = n % 10
        rev = (rem * 10) + rem
        n = n // 10
        return rev_num(n, rev)


    reversed1 = rev_num(n)
    reversed2 = rev_num(reversed1)

    return reversed2 == n