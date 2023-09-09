from termcolor import colored
#factorial function 
def fact(s):
  if s == 0:
    return 1
  else:
    return s * fact(s - 1)


print(colored("\t\t factorial using recursive function", 'blue'))
#get a input for user 
s = int(input("Enter a number: "))

if s < 0:
  print(colored("Factorial is not defined for negative numbers.",'red'))
else:
  result = fact(s)
  print(colored(f"The factorial of {s} is {result}", 'red'))
  