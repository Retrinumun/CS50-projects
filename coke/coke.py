accepted_coins = [5, 10, 25]
coke_total = 0
coin = int(input("Insert coins: "))
due = 50

while coke_total <= 50:
    if coin in accepted_coins:
        coke_total += coin
        due -= coin
        if due <= 0:
            due = due*-1
            print(f"Change owed: {due}")
            break

        else:
            print(f"Amount due: {due}")
            coin = int(input("Insert coin: "))

    else:
        print(f"Amount due: {due}")
        coin = int(input("Insert coin: "))
