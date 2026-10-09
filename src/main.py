#from datetime import date
#from utils import add, subtract, multiply

#print("Name: Abrar Ahmed Khan. Welcome to Github Basics")
#print("Today's Date:", date.today())

#print("Addition:", add(15,7))
#print("Subtraction:", subtract(15,7))
#print("Multiplication:", multiply(15,7))

#Updated
from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Your Full Name")
print("Today's Date:", date.today())

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divide(a, b))

except ValueError:
    print("Error: Please enter valid numbers.")

except TypeError as error:
    print("Error:", error)

except ZeroDivisionError as error:
    print("Error:", error)