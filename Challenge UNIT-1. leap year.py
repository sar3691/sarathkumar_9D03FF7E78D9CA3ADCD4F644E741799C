from termcolor import colored
print(colored("\t\tfind a leap year using if else",'blue'))
# Get the year from the user
year = int(input("Enter a year: ",))

# Check if it's a leap year
if year % 4 == 0 :
    print(colored(f"{year} is a leap year.", 'red'))
else:
    print(colored(f"{year} is not a leap year.", 'red'))
  