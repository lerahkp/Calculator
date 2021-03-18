#Calculator
from art import logo
#All Operations
def add(n1,n2):
  return n1 + n2
def substract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide,
}
def calculator():
  print(logo)

  num1 = float(input("What's the first number: "))
  for op in operations:
    print(op)
  should_cont = True
  while should_cont:
    op_sym = input("Choose an operations from the line above: ")
    num2 = float(input("What's the second number: "))
    calc_function = operations[op_sym]
    answer = calc_function(num1,num2)
    print(f"{num1} {op_sym} {num2} = {answer}")
    choice = input("Type 'y' to continue calculating with"+str(answer)+", or type 'n' to start a new: ")
    if choice == "y":
      num1=answer
    else:
      should_cont=False
      calculator()

calculator()