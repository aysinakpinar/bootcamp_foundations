num = 85
if num > 50:
    if num % 2 == 0:
        print(f"This number, {num}, is even and larger than 50!")
    elif num % 3 == 0:
        print(f"This nnumber, {num}, is divisible by 3 and larger than 50!")
    else:
        print(f"This number, {num}, is odd and not divisible by 3!")
else:
    print(f"This number, {num}, is too small")
    