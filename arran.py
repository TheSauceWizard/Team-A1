import time as t

print ("""
I approach the man.
"Hey, what brings you to this part of town?"
"Please sit Detective Frankestein, we have much to discuss."
My curosity compelled me to sit down.
"Who are you and how did you know my name?"
"My name is Chris Requiredfield.
I am working with Special Tactics and Resource Server or S.T.A.R.S to trackdown Hackula."
he procalims, taking a sip from his bottle "I knew your name because I worked with your father."
""")
t.sleep(2)
print(""""Why are you telling me this, what has it got to do with me?" I asked with frustration.
"This has everything to do with you.
Only you have enough data to resist his powers. You've done it before and must do it again."
"What do you mean? I have never even met 'Hackula,' I doubt he even exists." my voice raising in frustration.
"I understand that things may be confusing at the moment but all we explained over the next couple of days.
Meet me tomorrow at the church in town around 7 o'clock."
He hands me a map of Transfervania and took a final drink from his bottle, stands up and then leaves.
      """)
t.sleep(2)
print("""The night will soon become dawn. I grow weary. I book a room in the pub and I fall asleep quickly.
      """)
t.sleep(2)
print("""I wake up from the sound of a gentle breeze with no fatigue whatsoever. I rise from the double bed I slept in and check the clock mounted on the wall opposite me. It reads 14:01, I overslept. However, I still have 5 hours before I planned to meet with Chris.
 I can only do one thing before I meet with him.
      """)
variable1 = input("What do I do in that time? Investigate the town(1), Investigate around the pub(2) or Sleep until the time(3)")

if variable1 == "1":
        statement1 = False
    elif variable1 == "2":
        statement1 = False
    elif variable1 == "3":
        statement1 = False
    else:
        statement1 = True

print("""I leave my room going down the old wooden staircase, I find the pub to be empty.
""")

variable2 = input("Do i? Investigate the bar(1) Investigate the back alley(2) Go back and rest(3)")

if variable2 == "1":
        statement1 = False
    elif variable2 == "2":
        statement1 = False
    elif variable2 == "3":
        statement1 = False
    else:
        statement1 = True

print("""I look around the bar. There is nothing out of the ordinary and the bartender is no where to be seen.
""")

