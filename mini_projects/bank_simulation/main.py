from accounts import SavingsAccount, CurrentAccount

def main():
    # Create accounts
    acc1 = SavingsAccount("Alice", 20_000)
    acc2 = CurrentAccount("Bob", 5_000)

    # Deposits
    acc1.deposit(500)
    acc2.deposit(300)

    # Withdrawals
    acc1.withdraw(18_000)       # should fail (min balance rule)
    acc1.withdraw(1_000)        # should succeed

    acc2.withdraw(1_200)        # allowed (overdraft)
    acc2.withdraw(5_500)        # exceeds overdraft

    # Check balances
    print("\nFinal Balances:")
    print("Alice: ", acc1.get_balance())
    print("Bob: ", acc2.get_balance())

    # Show transactions
    print("Account 1 (savings account) transaction log")
    acc1.show_transactions()

    print("Account 2: (current account) transaction log")
    acc2.show_transactions()


if __name__ == "__main__":
    main()