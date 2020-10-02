# example if statements
print("You exit the taxi and arrive at the pub in Transfervania.")
print("You walk into the pub and see it is mostly empty. There's a bartender.")
print("As you walk up to the bar a girl runs towards you screaming")
print("Would you like to:")
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
        print("You ignore every word she says. The Cyborg Zombies escort her away.")
        statement1 = False
    else:
        statement1 = True
print("As I look around the pub I notice these things: the bartender is standing at the bar by himself,")
print(" the cyborg zombies have returned to the door, and an man sat in the corner of the room. ")

// hi it me
def story_telling():
    flag = True
    x = 0
    while flag == True:
        choice = (input("please enter 1,2 or 3"))
        if choice == "1":
            x += 1
            flag = False
        elif choice  == "2":
            x += 2
            flag = False
        elif choice == "3":
            x += 3
            flag = False
        else:
            flag = True
    return x

count = story_telling()
if count ==  1:
    count = story_telling(A[0]) //ignore this code thing its just me naming each option
    if count == 1:
         count = story_telling(A[1])
    elif count == 2:
        story_telling(B[0])
    else:
        story_telling(C[0])
elif count == 2:
    story_telling(B[0])
else:
    story_telling(C[0])

