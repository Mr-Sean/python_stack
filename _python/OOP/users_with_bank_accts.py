# Update your existing User class to have an association with the BankAccount class. 
# You should not have to change anything in the BankAccount class. 
# The method signatures of the User class (the first line of the method with the def keyword) should also remain the same.

# For example, our User class currently has a method like this:

# class User:
#     # other methods
#     def make_deposit(self, amount):
#         self.account_balance += amount	# hmmm...the User class doesn't have an account_balance attribute anymore

# But for this assignment, our User class will no longer have a self.account_balance attribute. 
# Instead, we will replace this attribute's value in our __init__ method with an instance of a BankAccount, and use the name of self.account. 
# That means our make_deposit (and other methods referencing self.account_balance) need to be updated! That's the goal of this assignment.

# Remember in our User methods, we are going to now be accessing the BankAccount class through our self.account attribute, like so:

# class User:
#     def example_method(self):
#         self.account.deposit(100)		# we can call the BankAccount instance's methods
#         print(self.account.balance)		# or access its attributes


# Make sure that by the end of this assignment that you:

# have both the User and BankAccount classes in the same file for your assignment
# only create BankAccount instances inside of the User's __init__ method
# only call BankAccount methods inside of the methods in the User class


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

# ------------------------------------------------------------

# Update the User class __init__ method  
# Update the User class make_deposit method  
# Update the User class make_withdrawal method  
# Update the User class display_user_balance method  
# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.1) #(Int rate only, Balance=0 so left blank)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

sean = User("Sean", "sean@gmail.com")
sean.make_deposit(100).make_withdrawal(75).display_user_balance()
sean.account.yield_interest().display_account_info()
sean.display_user_balance()