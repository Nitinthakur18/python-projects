import art
print("Welcome to the secret auction program.")
print(art.logo)

bid={}
want_to_continue=True
while want_to_continue:
    name=input("What is your name?:")
    amount=int(input("What is your bid?: $"))
    bid[name]=amount
    should_continue=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue=="no":
        want_to_continue=False
    elif should_continue=="yes":
        want_to_continue=True
        print("\n"*100)
maxi=max(bid, key=bid.get)
print(f"The winner is {maxi} with a bid of ${bid[maxi]}.")