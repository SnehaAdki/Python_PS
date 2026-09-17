class Account(): 

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self , deposite_amount):
        self.balance = self.balance + deposite_amount
        print("Deposite Accepted!...")

    def withdraw(self , withdrawl_amount):
        if self.balance >  withdrawl_amount:
            print("Funds Unavailable!... ")
        else:
            self.balance -= withdrawl_amount
            print("Withdrawl Accepted!...")

    def __str__(self):
        return f"Account Owner : {self.owner} \nAccount Balance : {self.balance}"

a1 = Account('Sneha',100)
print(a1)
a1.deposite(50)
print("After Deposite!...")
print(a1)
a1.withdraw(60)
print("After Withdrawl!...")
print(a1)
a1.withdraw(100)

print(a1)