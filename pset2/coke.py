def main():
    # variables for amt paid and owed
    amt_paid = 0
    amt_owed = 50
    # while the amt owed is > 0
    while amt_owed > 0:
        # print amt owed
        print(f"Amount Due: {amt_owed}")
        # user input for money
        money = int(input("Insert Coin: "))
        # validating the correct coins
        if money == 5 or money == 10 or money == 25:
            # the amt paid updates
            amt_paid += money
            # amt owed updates
            amt_owed = 50 - amt_paid
    # calculating change
    change = amt_paid - 50
    # print change owed
    print(f"Change Owed: {change}")

main()
