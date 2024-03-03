import datetime

class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def get_transactions_history(self):
        return self.transaction_history

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append((datetime.datetime.now(), "Withdraw", amount))
            return True
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append((datetime.datetime.now(), "Deposit", amount))
            return True
        else:
            return False

    def transfer(self, to_user, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            to_user.balance += amount
            self.transaction_history.append((datetime.datetime.now(), "Transfer to user id:" + to_user.user_id, amount))
            to_user.transaction_history.append((datetime.datetime.now(), "Transfer from User ID:" + self.user_id, amount))
            return True
        else:
            return False

class ATM:
    def __init__(self):
        self.users = {}

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None

    def add_user(self, user):
        self.users[user.user_id] = user

def main():
    atm = ATM()
    # user ID and PIN
    kavitha = User("kavitha", "123")
    naveen = User("naveen", "456")

    atm.add_user(kavitha)
    atm.add_user(naveen)

    while True:
        print("Welcome To My ATM Interface")
        user_id = input("Enter the User ID: ")
        pin = input("Enter the PIN: ")
        user = atm.authenticate_user(user_id, pin)

        if user:
            print("Successfully Authenticated")
            while True:
                print("1. Transactions history")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Transfer")
                print("5. Quit")

                choice = input("Enter your Choice: ")
                if choice == "1":
                    print("Transaction history: ")
                    for transactions in user.get_transactions_history():
                        print(transactions)
                elif choice == "2":
                    amount = float(input("Enter the Withdrawal Amount: "))
                    if user.withdraw(amount):
                        print("Successfully Withdrawn. Now Your Balance is: ", user.balance)
                    else:
                        print("Invalid Amount or Insufficient Balance")
                elif choice == "3":
                    amount = float(input("Enter the Deposit Amount: "))
                    if user.deposit(amount):
                        print("Successfully Deposited. Now Your Balance is: ", user.balance)
                    else:
                        print("Invalid Amount. Please Enter a Valid Amount")
                elif choice == "4":
                    recipient_id = input("Enter The Recipient's User ID: ")
                    recipient = atm.authenticate_user(recipient_id, "1111")
                    if recipient:
                        amount = float(input("Enter The Transfer Amount: "))
                        if user.transfer(recipient, amount):
                            print("Successfully Transferred")
                        else:
                            print("Invalid Amount or Insufficient Balance")
                    else:
                        print("Recipient Not Found")
                elif choice == "5":
                    print("Thank You For Using The ATM!")
                    exit()
                else:
                    print("Invalid Choice. Please Select a Valid Option")
        else:
            print("Authentication Failed. Please Check Your User ID and PIN")

if __name__ == "__main__":
    # call the main function
    main()