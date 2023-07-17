class Calculator:

    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def addition(self):
        result = self._num1 + self._num2
        print(f"{self._num1} + {self._num2} = {result}")
      
    def multiply(self):
        result = self._num1 * self._num2
        print(f"{self._num1} * {self._num2} = {result}")
      
    def subtract(self):
        result = self._num1 - self._num2
        print(f"{self._num1} - {self._num2} = {result}")
        
    def divide(self):
      if self._num2 == 0:
        print("Error:cannot divide number by zero")
      else: 
        result = self._num1 / self._num2
        print(f"{self._num1} / {self._num2} = {result}")


def calculator_run():
  
  while True:
     try:
       num1 = float(input("Enter the first number: "))
       break
     except ValueError:
      print("Error: Must enter a valid number")
    

  while True:
      operator = input("Enter an operator (+, -, *, /): ")
      operators = ['+', '-', '*', '/']
      if operator not in operators:
        print("Error: Enter a valid operator(+, -, *, /)")
      else:
        break

  while True:
     try:
       num2 = float(input("Enter the second number: "))
       break
     except ValueError:
       print("Error: Must enter a valid number")
    

  

  calculate = Calculator(num1,num2)
 
  if operator == '+':
    calculate.addition()
  elif operator == '-':
    calculate.subtract()
  elif operator == '*':
    calculate.multiply()
  elif operator == '/':
    calculate.divide()


  cont = input("Run again? 'y/n'")
  if cont.strip().lower() == "y":
        calculator_run()
  else:
        exit()
  
calculator_run()

