from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, bal=0):
        self._owner = owner
        self.__balance = bal
        self._transactions = []

    
    def get_balance(self):
        return self.__balance
    
    # internal method to update balance safely.    
    def _update_balance(self, amt):
        self.__balance += amt

    
    # not an abstract method because the implementation is the same for all child classes    
    def deposit(self, amt):
        if amt <= 0:
            print("Invalid deposit amount")
            return
        
        self._update_balance(amt)
        self._transactions.append(f"Deposit: {amt}")
        print(f"deposit successful: deposited {amt}/-")
    
    
    # abstract method bcz all accounts must implement it, and the implementation varies for different child classes.
    @abstractmethod
    def withdraw(amt):
        pass


    # shows transaction history. Implement later!
    def show_transactions(self):
        for transaction in self._transactions:
            print(transaction)
    
    


class SavingsAccount(Account):
    MIN_BALANCE = 5000

    def withdraw(self, amt):
        if amt <= 0:
            print("Invalid withdraw amount")
            return False

        if (self.get_balance() - amt) > self.MIN_BALANCE:
            self._update_balance(-amt)
            self._transactions.append(f"Withdrawl: {amt}")
            print(f"withdrew {amt}/- successfully")
            return True

        else:
            print("Insufficient funds! Minimum balance must be maintained")
            return False



class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000

    def withdraw(self, amt):
        if amt <= 0:
            print("Invalid withdraw amount")
            return False

        if (self.get_balance() + self.OVERDRAFT_LIMIT) > amt:
            self._update_balance(-amt)
            print(f"withdrew {amt}/- successfully")
            self._transactions.append(f"Withdrawl: {amt}")
            return True

        else:
            print("cannot withdraw: overdraft limit exceeded")
            return False



def main():
    # Create accounts
    acc1 = SavingsAccount("Alice", 20_000)
    acc2 = CurrentAccount("Bob", 5_000)

    # Deposits
    acc1.deposit(500)
    acc2.deposit(300)

    # Withdrawals
    acc1.withdraw(18_000)   # should fail (min balance rule)
    acc1.withdraw(1_000)   # should succeed

    acc2.withdraw(1_200)   # allowed (overdraft)
    acc2.withdraw(5_500)    # may exceed overdraft

    # Check balances
    print("\nFinal Balances:")
    print("Alice:", acc1.get_balance())
    print("Bob:", acc2.get_balance())

    # Show transactions
    acc1.show_transactions()
    acc2.show_transactions()



if __name__ == "__main__":
    main()

"""
# work with customer name for now. Use customer id when learning about static variables
class Customer:
    def __init__(self, name, year_of_birth, phone_no=None, email=None):
        self.name = name
        self.year_of_birth = year_of_birth
        self.phone_no = phone_no
        self.email = email

    def update_phone(self, phone):
        ...


    def update_email(self, email):
        ...


    def show_info(self):
        ...

""" 