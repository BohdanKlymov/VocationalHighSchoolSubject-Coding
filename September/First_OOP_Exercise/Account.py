Class Account:

    def __init__ (self, account_num: int, owner: str, balance: float):
        self.account_num = account_num
        self.owner = owner
        self.balance = balance

    def setOwner(self, neu_owner: String):
        self.owner = neu_owner

    def setAccountNum(self, neu_account_num: int):
        self.account_num = neu_account_num
    
    def getOwner(self):
        return self.owner

    def getAccount_num(self):
        return self.account_num

    def getBalance(self):
        return self.balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def pay_out (self, amount: float):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Payout amount must be positive and less than or equal to the current balance.")
