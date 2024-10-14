#Nathaniel Castro ProfTest: What is happening? For Comments

class BankAccount:
    def __init__(self, account_number, balance=0): 
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): #Lets user put money into the account
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):#Lets user take money from the account
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):#Asks user how much money they have
        return self.balance

def create_account(): #Lets user make account variable and how much is in it
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)

def main():#Asks for a number 1-5
    accounts = {}
    while True:#If any of the number 1-5 was chose its respective print statement will follow
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1': #if 1 ischosen it will create account
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']: #if 2,3,4 are chosen something else happens
            account_number = input("Enter account number: ")
            if account_number in accounts: # If the account number is found it takes you to the option 2,3,4,
                account = accounts[account_number]
                if choice == '2': # Asks user hoe much they would like to add
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount): #If they added anything it says how much they then have
                        print(f"Deposited ${amount:.2f} successfully!")
                    else: # If the dont have the money to deposit it doesnt work
                        print("Invalid deposit amount.")
                elif choice == '3': #if the user chose 3 they are allowed to take money 
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount): # If they have enough money to take it works
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else: # If they dont have money then they cant withdraw
                        print("Invalid withdrawal amount or insufficient funds.")
                else: # Shows user how mcuh moey they currently have
                    print(f"Current balance: ${account.get_balance():.2f}")
            else:#If they dont have an account yet it doesnt work
                print("Account not found.")
        
        elif choice == '5': # If the user chose 5 it closes the system
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else: # If any other number is chose it has error
            print("Invalid choice. Please try again.")

if __name__ == "__main__": 
    main()
