def add(x, y):
  return x + y


def subtract(x, y):
  return x - y


def multiply(x, y):
  return x * y


def divide(x, y):
  if y == 0:
    raise ValueError("Cannot divide by zero")
  return x / y


def main():
  print("Hi, I'm your SimCal, a simple calculator. :)")

  while True:
    print("\nWhat would you like to do?\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice.upper() == '5':
      print("\nThank you for using SimCal!")
      break
    elif choice.upper() in ['1', '2', '3', '4']:
      operation = ""
      if choice.upper() == '1':
        operation = "Addition"
      elif choice.upper() == '2':
        operation = "Subtraction"
      elif choice.upper() == '3':
        operation = "Multiplication"
      elif choice.upper() == '4':
        operation = "Division"

      print(f"\nGreat! You chose {operation}.")
      try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("\nEnter the second number: "))
        if choice.upper() == '1':
          result = add(num1, num2)
        elif choice.upper() == '2':
          result = subtract(num1, num2)
        elif choice.upper() == '3':
          result = multiply(num1, num2)
        elif choice.upper() == '4':
          result = divide(num1, num2)

        print("\nEasy, the answer is: ", result)
      except ValueError as e:
        print("\nError:", e)
    else:
      print("\nInvalid choice. Please enter a number between 1 to 5 only.")


if __name__ == "__main__":
  main()
