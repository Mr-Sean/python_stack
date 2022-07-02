# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount

# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; 
#     if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5

# display_account_info(self) - print to the console: eg. "Balance: $100"

# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)


# This means we need a class that looks something like this:

# class BankAccount:
# 	def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
# 		# your code here! (remember, this is where we specify the attributes for our class)
#         # don't worry about user info here; we'll involve the User class soon
# 	def deposit(self, amount):
# 		# your code here
# 	def withdraw(self, amount):
# 		# your code here
# 	def display_account_info(self):
# 		# your code here
# 	def yield_interest(self):
# 		# your code here

# Create a BankAccount class with the attributes interest rate and balance  

# Add a deposit method to the BankAccount class  

# Add a withdraw method to the BankAccount class  

# Add a display_account_info method to the BankAccount class  

# Add a yield_interest method to the BankAccount class  



# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, 
# the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. 
# The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), 
# which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

class BankAccount:
    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if(self.balance >= 0):
            self.balance += self.balance*self.int_rate
        return self


checking = BankAccount(0.1, 500)
savings = BankAccount(0.25, 1000)

# Create 2 accounts  
# To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)  
# To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)
checking.deposit(100).deposit(200).deposit(50).withdraw(150).yield_interest().display_account_info()
savings.deposit(175).deposit(220).withdraw(200).withdraw(120).withdraw(75).withdraw(300).yield_interest().display_account_info()