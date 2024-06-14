import sys
x = int(input("x: "))
y = int(input("y: "))

try:
    result = (x / y )
except Exception as error:
    print(f"{error.__class__.__name__}")
    sys.exit(1)
    
print(f"{x} / {y} = {result}")