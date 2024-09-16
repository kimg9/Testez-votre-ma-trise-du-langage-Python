## Écrivez votre code ici !
class BankAccount():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if isinstance(amount, int):
            if amount < 0:
                return print(f"Vous avez entré {amount}. Vous ne pouvez pas entrer un nombre négatif pour effectuer un dépôt.\n")
            else:
                self.balance += amount
        else:
            return print(f"Vous avez entré {amount}. Merci de n'entrer qu'un nombre commme montant du dépôt.\n")

    def withdraw(self, amount):
        if isinstance(amount, int):
            if self.balance - amount < 0:
                return print(f"Vous avez entré {amount} et votre balance est {self.balance}. Vous n'avez pas assez de fond pour effectuer ce retrait.\n")
            else:
                self.balance -= amount
        else:
            return print(f"Vous avez entré {amount}. Merci de n'entrer qu'un nombre commme montant du dépôt.")

    def display_balance(self):
        return print(f"Compte de {self.account_holder} \n  Solde de : {self.balance}\n")

bank_account = BankAccount(account_holder="John Doe", balance=50)
bank_account.display_balance()
bank_account.deposit(100)
bank_account.display_balance()
bank_account.deposit(-100)
bank_account.deposit("abc")
bank_account.withdraw(50)
bank_account.display_balance()
bank_account.withdraw(120)
bank_account.display_balance()
