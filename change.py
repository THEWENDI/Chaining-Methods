class User:
    def __init__(self, name,):
        self.name = name
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_balance(self):
        print("User: ", self.name, "Balance: ", self.account_balance)
        return self

    def transfer_money(self, user, amount):
        self.account_balance -= amount
        user.account_balance += amount 
        self.display_balance()
        user.display_balance()
        return self

user = User("Mr.x")
# print(user.__dict__)
user.deposit(300).deposit(300).deposit(400).withdrawal(200).display_balance()

user2 = User("Mr.y")

user2.deposit(1000).deposit(1000).withdrawal(500).withdrawal(500).display_balance()

user3 = User("Mr.z")

user3.deposit(10000).withdrawal(1000).withdrawal(1000).withdrawal(1000).display_balance().transfer_money(user2,2000)

