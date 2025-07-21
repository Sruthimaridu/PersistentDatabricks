try:
    res=10/0
except ZeroDivisionError:
    print("cannot divide by Zero")

#######################################
try:
    value=int(input("enter num:"))
    res=10/value
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("cannot divide by zero")
##################################
try:
    value=int(input("enter num:"))
    res=10/value
except(ValueError,TypeError,ZeroDivisionError) as e:
    print(f"an error occured:{e}")
