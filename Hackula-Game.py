# example if statements
print("You exit the taxi and arrive at the pub in Transfervania.")
print("You walk into the pub and see it is mostly empty. There's a bartender.")
print("As you walk up to the bar a girl runs towards you screaming")
print("Woukd you like to:")
print("1. Listen to her.")
print("2. Ignore her.")
statement1 = True
while statement1 == True:
    option1 = int(input("Enter 1 or 2"))
    if option1 == 1:
        print("“Hackula, he’s back. You’re Frankenstein's lad, aren't you?")
        print("You are the only one strong enough to stop him. Please, you must kill him to save our town")
        statement1 = False
    elif option1 == 2:
        print("You ignore every word she says. The Zombie cyborgs escort her away.")
        statement1 = False
    else:
        statement1 = True
