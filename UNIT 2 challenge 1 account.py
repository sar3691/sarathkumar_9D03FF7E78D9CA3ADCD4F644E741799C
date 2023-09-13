class Bank_Account :
    def __init__(self, acc_num, acc_name, acc_bal=0.0):
        self._acc_num = acc_num
        self._acc_name = acc_name
        self._acc_bal = acc_bal
    def holder(self):
        print("acc_num\t\tname\t     balance")
        print(self._acc_num,"\t",self._acc_name,"\t",self._acc_bal)
    def deposit(self, amount):
        if amount > 0:
            self._acc_bal += amount
            return f"Deposited ₹{amount}. New balance: ₹{self._acc_bal}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self._acc_bal:
            self._acc_bal -= amount
            return f"Withdrew ₹{amount}. New balance: ₹{self._acc_bal}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_balance(self):
        return f"Account Balance for {self._acc_name}: ₹{self._acc_bal}"

# Testing the BankAccount class
if __name__ == "__main__":
    from termcolor import colored
    print(colored("\t\t\t\t BANK ACCOUNT \n\n\n",'blue'))
    # Create an instance of BankAccount
    acc = Bank_Account("3691215", "sarath", 1000.0)
    
    # Test deposit and withdrawal functionality
    acc.holder()
    print("\n\n\n")
    print(acc.display_balance(),"\n\n\n")
    A=int(input("ender deposited ammount "))
    d=acc.deposit(A)
    print(d,"\n\n\n")
    B=int(input("enter the withdrawal ammount "))
    
    print(acc.withdraw(B))