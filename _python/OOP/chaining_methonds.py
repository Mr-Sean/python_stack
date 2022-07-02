# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.
# For this assignment, we'll add some functionality to the User class:

# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150

# Create a file with the User class, including the __init__ and make_deposit methods  

# Add a make_withdrawal method to the User class  

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

# Add a display_user_balance method to the User class  
    def display_user_balance(self):
        print(self.account_balance)
        return self

# BONUS: transfer_money(self, other_user, amount) - have this method decrease the 
# user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self

# sean = User("Sean", "sean@gmail.com")
# mydeposit = sean.make_deposit(10)  # Does NOT need "mydeposit" variable to run. Var is optional.
# sean.make_withdrawal(15)
# sean.display_user_balance()

# Create 3 instances of the User class  
tony = User('Tony', 'tony@gmail.com')
jimmy = User('Jimmy', 'jimmy@gmail.com')
danny = User('Danny', 'danny@gmail.com')

# Have the first user make 3 deposits and 1 withdrawal and then display their balance  
tony.make_deposit(10).make_deposit(15).make_deposit(5).make_withdrawal(20).display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance  
jimmy.make_deposit(20).make_deposit(30).make_withdrawal(10).make_withdrawal(5).display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance  
danny.make_deposit(100).make_withdrawal(20).make_withdrawal(30).make_withdrawal(25).display_user_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
danny.transfer_money(tony,12)
danny.display_user_balance()
tony.display_user_balance()