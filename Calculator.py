def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  if a == 0:
    raise ZeroDivisionError("Cannot divide by zero")
  return a / b
print("Welcome.......")
while True:
  operation = input("Select operation want to perform(+, -, *, /):")
  try:
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    if operation == "+":
      result = add(a, b)
    elif operation == "-":
      result = subtract(a, b)
    elif operation == "*":
      result = multiply(a, b)
    elif operation == "/":
      result = divide(a, b)
    else:
      print("Invalid operation!!!")
      continue
    print("Result:", result)
  except ValueError:
    print("Invalid input. Please enter valid number..")
  except ZeroDivisionError as e:
    print(e)
  choice = input("Continue (y/n)? ")
  if choice != "y":
    break