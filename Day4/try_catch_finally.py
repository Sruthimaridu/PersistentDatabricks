try:
    
    
    #file=open('data.txt','r')
    #data=file.read()
    #num=int(data)
    value=int(input("enter num"))
    result=10/value
except ZeroDivisionError:
    print("divide by zero error")
except ValueError:
    print("invalid data")
else:
    print(f"sccesssfully divided:{value}")
finally:
    print("project execution completed")