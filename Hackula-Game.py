#example if statements
print("You exit the taxi and arrive at the pub in Transfervania.")
print("You walk into the pub and see it is mostly empty. There's a bartender.")
print("As you walk up to the bar a girl runs towards you screaming")
statement = true
option = int(input("1, 2 or 3"))
while statement == True:
  if option == 1:
   statement = False  
  
  elif option == 2:
    statement = False
  
  elif option == 3:
    statement = False
  
  else:
    statement = True
