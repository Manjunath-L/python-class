def opp(n):
  # your solution here
    if n > 0:
        return float(f"-{n}")
    elif n < 0:
        return float(f"{n}")
    else:
        return 0
    
print(opp(-3.1458))