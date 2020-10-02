    # example if statements
back = True
bartender = False
play = True


def postsleep():
    print("""

I wake up on the arm chair in my room. I look out the window and see that the streets are already dark.
I look up to the clock and see that the time is half-past six.
I should go and meet Chris. 
""")
    input()
    print("""

I down the familiar staircase and pass through the quiet pub. I leave through the front door into the cold streets. I check the map Chris gave me then I walk towards the church. 

As I approach the church I see Chris stood in a thick, black trenchcoat. 
"Let's go. Hackula will be strongest at midnight tonight. Take this McAfee Anti-virus, it will help you resist his power."

1. Take Anti-Virus
2. Refuse it
""")
    choice7 = int(input("enter 1 or 2 "))
    if choice7 == 2:
        print("Game Over")
        input()
        exit()
    else:
        print("""

You take the McAfee pill. It has an unpleasant and bitter taste but I can feel it improve my mental fortitude.
""")
        input()
        print("""

I walk with Chris towards the castle on the outskirts of the town. T
he fullmoon still lay low in the night sky.
The castle itself was dark however I still saw the gothic towers that poked the stary sky and the large, unwelcoming walls. 

Chris and I made it to the front gate without seeing a soul in sight,
though it was so dark I'm unsure if souls would have seen us either. The gate remained shut. Should I...

    1. Knock on the gate
    2. Attempt to jump over
""")
        choice9 = int(input("enter 1 or 2"))
        if choice9 == 2:
            print("""

I attempt to climb over the gate. As I begin to climb the gate my limbs start moving slower and slower. I drop from the gate in exhaustion. 
"When was the last time you updated your drivers?" Chris crys out, "perhaps it wasn't a good idea to give you that pill, the software is pretty new."
"These parts sure aren't new" I panted. 
"I guess we should try something else"
""")
            input("Knock on the gate")

        print("""

With my massive fists I thud the grand gate. I feel the cold steel reverbarate. 
The gates open by them selves almost as if we were being invited in.
As we walk through the castle garden I cannot help but feel like we are being watched. 
In front of us we see the front door and to the side us are windows, one which is smashed open. 
Do we...

    1. Sneak in
    2. Go through the door
""")
        choice10 = int(input("enter 1 or 2"))
        if choice10 == 2:
            print("""

We sneak through the window. However, whatever is in here with us knows where we are. 
Within a blink of an eye a massive ball of energy passes through Chris.
He clutches his head in pain, wriggling across the floor as his eyes turn blood red. He then passed out. 
I have to leave him behind, there must be a way out of this. 
""")
            input()
        print("""

An ominous air fills the room, the dim glow of the monitors reflected at me.
I hear the wind howling, a window flutters open. Suddenly, there he is in all his magnificence.
Tall, dark and handsome. His blood-red eyes glistening in the cold light.
His crooked smile, showing his high speed 16 Gb USB Flash Drive teeth. My muscles tighten, I am unable to move.
Is he doing this or am I simply too in awe to move in the sight of this enigmatic dashing figure?
Emotions come rushing to me, fear, hatred, dread and a little bit of arousal.
Whatever this creature before me is, it’s clear he’s having an unknown effect on my cyber-brain. 
""")
        input()
        print("""
I launch myself towards Hackula.
If only Chris was here, he'd know what to do. 

Do I...
    1. Remove his head
    2. Beat him to death with his own arm
""")
        choice11 = int(input("enter 1 or 2 "))

        if choice11 == 1:
            print("""

I grab Hackula's skull with my enormous arms. He grabs my head too. 
I feel his red eyes piercing into my skull but the McAfee pill begins to cause Hackula to yelp.
I start pulling at his head with all the force I could manage. 
After several seconds of pulling, his head pulls out like a plug from a socket.
His body spasms for a second before dropping to the floor. His head evaporates in my hands, his last expression being one of fear. 

We've won. 
""")
            input()
            print("""

As the sun rises for a new dawn I sit with Chris.
I look upon Transfervania and see a new hope for it's people because they are free of the curse of Hackula.
All the men, women and monsters can make memories without fear of losing them.

~~
You have achieved the good ending
""")
            input()
            exit()
                    
        elif choice11 == 2:
            print("""

I grab his arm and Hackula grabs my head. 
I feel his red eyes piercing into my skull but the McAfee pill begins to cause Hackula to yelp.
I start pulling at his arm off with all the force I could manage. 
After I succeed I begin to flail him without mercy. However, Hackula just laughs.
He rises with grace. Small mechanisms rebuild his lost arm while the one I am holding evaporated. 

"Why won't you die?" I exclaim.

"Nano-machines son. They harden in responce to physical trauma. You can't hurt me Frank." he brags.

Do I...

    1. Attempt to remove his head
    2. Run away
""")
            choice12  = int(input("enter 1 or 2 "))
            if choice12 == 1:
                print("""
I grab Hackula's skull with my enormous arms. He grabs my head too. 
I feel his red eyes piercing into my skull and my memories begin leave my head. The anti-virus has worn off.
Come to think of it I cannot remember anything before I came here other than my early childhood. How many times has this happened...
Am I only continuing the cycle?
If I lose my memories, am I really the same person as before. Is it the death of my ego? I...
""")
                input()
                print("""

I wake up at a pub. How did I get here?
What is this in my pocket? A map of Transfervania!
Perhaps I will find answers there.

~~
You have achieved the bad ending.
""")
                input()
                exit()
                        
            elif choice12 == 2:
                    print("""
I leave Chris behind and run with tears pouring down my face. My heart beat accelerates.
I make it through the gate at the entrance to the castle yet I still hear the cackles of Hackula. 
I decide to leave the fate of Transfervania to Hackula. I will leave this town tonight. I am sorry Chris

~~
You have achieved the coward's ending
""")
                    input()
                    exit()
while play == True:
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

    while back == True: 
        print("As I look around the pub I notice these things: the bartender is standing at the bar by himself,")
        print(" the cyborg zombies have returned to the door, and an man sat in the corner of the room. ")
        print("Would you like to:")
        print("1. Speak to the bartender")
        print("2. Speak to the Cyborg Zombies")
        print("3. Speak to man")

        back = False
        choice_1 = int(input("enter 1, 2 or 3"))
        if choice_1 == 1:
            bartender = True

        elif choice_1 == 2:
            print("""

I approach the Cyborg Zombies.
"What happened with that girl who just came?" I ask. 
"BOOTING RESPONSE... 
...
...
BRAAAAAAAAINZ!"
I don't know what I was expecting. 
""")
            input()
            back = True

        while bartender == True and back == False:
            bartender = False
            back = False
        
            print("""

I approach the bartender.
"What will it be?" He says in an assertive tone.

    1. Ask for another drink
    2. Ask for information about the girl who just came in
    3. Go back
""")

            choice = int(input("enter 1, 2 or 3"))

            if choice == 1:
                print("""

What drink would you like?

    1. Water
    2. Bourbon and Gasoline
    3. Screenshots
                """)
                choice1 = int(input("enter 1, 2 or 3"))
                if choice1 == 1:
                    print("""

He passes me a jug of water.I step away from the bar to have my drink.
It was pleasant, fresh and just cooler than room tempreture.
Perhaps this water was taken from the local Apuseni Mountains.
                    """)

                    bartender = True

                elif choice1 == 2:
                    print("""

He places a polished whiskey glass onto the counter.
He places two icecubes into the bottom of the glass then he pours bourbon from a bottle into the glass.
He then adds gasoline to the glass, allowing it to sit above the bourbon before stirring it for around 7 seconds.
I step away from the bar with my drink and then taste it.
Although I had before it still left me more than impressed. It's very tasty. Maybe I should get this again.
                    """)
                    bartender = True
                    
                elif choice1 == 3:
                    print("""

He places a small shot glass onto the counter.
He takes out a small, unlabeled bottle from under the counter and then poured it gently into glass.
It was an unsual blue colour with a milk like vicosity. I downed it quickly.
At first it had a snappy spice but then it developed into a smooth taste in the mouth.
This is why he kept it in an unlabeled bottle, to keep it a secret. 
                    """)
                    bartender == True
                    
                else:
                    input()
                    
                print("""

you drink and head back to the bartender...
""")
                bartender = True
                input()
            elif choice == 2:
                print("""
            
"Who was that girl who just came and left?" 
"A local lass, I've seen her around here a few times now looking for help" the bartender said, cleaning a glass. 
"Why does she need help?"
He leans over the counter "Her parents recently lost all of their memory and it broke her damn heart. S
he now goes around claiming 'Hackula' did it and asking the strongest men and women she sees to kill him."
"I thought 'Hackula' was a story they told to children to teach them to keep their data safe." I said, my fingers twiddling. 
"I hope it just a story" the bartender murmured now walking to the back of the bar to clean.

    1. Speak to the bartender
    2. Go back
        """)
                choice2 = int(input("enter 1 or 2"))
                if choice2 == 1:
                    bartender = True
                else:
                    back = True

            elif choice == 3:
                back = True
        if choice_1 == 3:
            print("""

I approach the man.
"Hey, what brings you to this part of town?"
"Please sit Detective Frankestein, we have much to discuss."
My curosity compelled me to sit down.
"Who are you and how did you know my name?"
"My name is Chris Requiredfield. I am working with Special Tactics and Resource Server or S.T.A.R.S to trackdown
Hackula." he procalims, taking a sip from his bottle "I knew your name because I worked with your father."
""")
            input()
            print("""

"Why are you telling me this, what has it got to do with me?" I asked with frustration.
"This has everything to do with you. Only you have enough data to resist his powers.
You've done it before and must do it again."
"What do you mean? I have never even met 'Hackula,' I doubt he even exists.
" my voice raising in frustration. 
"I understand that things may be confusing at the moment but all we explained over the next couple of days.
Meet me tomorrow at the church in town around 7 o'clock."
He hands me a map of Transfervania and took a final drink from his bottle, stands up and then leaves.
""")
            input()
            print("""

The night will soon become dawn. I grow weary.
I book a room in the pub and I fall asleep quickly.
""")
            input()
            print("""

I wake up from the sound of a gentle breeze with no fatigue whatsoever.
I rise from the double bed I slept in and check the clock mounted on the wall opposite me.
It reads 14:01, I overslept. However, I still have 5 hours before I planned to meet with Chris.
I can only do one thing before I meet with him. What do I do in that time?

    1. Investigate the town
    2. Investigate the pub
    3. Sleep until time
    """)

            choice3 = int(input("enter 1, 2 or 3 "))
            if choice3 == 3:
                postsleep()
            elif choice3 == 2:
                print("""

I leave my room going down the old wooden staircase, I find the pub to be empty.

Do I...

    1. Investigate the Bar
    2. Investigate the back alley
    3. Go back and rest

""")
                choice13 = int(input("enter 1, 2 or 3 "))
                if choice13 == 3:
                    postsleep()
                elif choice13 == 1:
                    print("""

I look around the bar. There is nothing out of the ordinary and the bartender is no where to be seen.

    1.Investigate the back alley
    2. Go back and rest
""")
                choice14 = int(input("enter 1 or 2"))
                if choice14 == 2:
                    postsleep()

                print("""
I go through the back door the girl ran through last night.
I look around and don't see anything out of the ordinary. 
"What's that?" I exclaim. 
I see glistening blonde hair on the floor.
I go up to it and investigate it. I see a trail of these hairs, as if she had been dragged. 
""")
                input("follow the hairs")
                print("""

I follow the hairs across several alleys until I reach an iron door. I feel an evil aura on the inside.
As I get closer I feel sicker and sicker until eventually fear consumes my body.
I think it would be a really bad idea to continue.

    1. Continue anyway
    2. Retreat
    
""")
                choice15 = int(input("enter 1 or 2"))
                if choice15 == 1:
                    print("""
I open the door...
I walk into the dark room and the door slams.
Through the small bit of light going through the cracks in the door I see a shadowy figure.
The figure lights a candle besides him.
""")
                    input()
                    print("""

"Back again so soon Frank," the figure says in a dominant tone, "I thought you'd stay away for good this time."
"Who the hell are you?" I demanded, staying perfectly still. 
"I am the one men, women, and IT consultants all fear. King of the Dark Web and taker of data. I am Lord Hackula!"
I take one step closer to him, he stays there completely still.
"Oh so you are approaching me" he says in a mocking tone "most people run when they first catch a glimpse of me.
Clearly your Father gave you the brain of an idiot."
""")
                    input()
                    print("""
"What are you doing here? What happened to the girl?" I demanded. 
Hackula let out a short chuckle. His face still in the shadows he stood up. 
"I doubt she remembers our encounter, and neither will you."
He dashes towards me his arms preparing to grab me. 
Before I can react his hands grasp my head. Through the darkness I see his dark, red eyes. I feel my memories seeping out from my head, being stolen by this menace.
I start to lose consciousness. I...
""")
                    input()
                    postsleep()
                elif choice15 == 2:
                    print("""

I take several steps back. The aura reduces in intensity. I head back the way I came and enter the pub. I need to rest
""")
                    input()
                    postsleep()
                        

            elif choice3 == 1:
                print("""

    I leave my room going down the old wooden staircase, I pass through the empty pub and head through the front door.
    A bitter frost has filled the streets, the air cold and crisp, keeping my internal parts cold without the need for
    activating my many different cooling subroutines. 
    I step outside to find a newspaper, shaking off the dirt and frost I had found it was The Transfervlynia Times. 
    The main headline read “5th memory wipe victim of the month found last night” and “Rumours of the terrifying Hackula escalate fears”. 
    It was hard to deny there was something uncanny happening here.
    I look around and I see nobody is around. 
    Do I...

        1. Continue into town
        2. Rest
    """)
                choice4 = int(input("enter 1 or 2 "))
                if choice4 == 2:
                    postsleep()

                elif choice4 == 1:
                    print("""

    As I wonder into town the streets are cold and bare.
    The markets were shut down and the shops were run down. Not even the ghosts inhabited this ghost town.
    All of the men, women and monsters must have abandoned this part of town. Is this Hackula's doing?
    """)
                    input()
                    print("""

    As I reach the town hall, I notice there is a single light beaming on the first floor.
    I approach the giant double doors and knock on the ancient oak causing a massive thud and
    knocking snow off the roof and the windowsills. 
    The light suddenly turns off. 
    I guess whoever was in there didn't want any guests.

        1. Knock Again
        2. Go back and rest

    """)
                    choice5 = int(input("enter 1 or 2 "))
                    if choice5 == 1:
                        done = False
                        while done == False:
                            print("""

    I knock again. There is still no answer.
        1. Knock again
        2. Go back and rest
    """)
                            choice6 = int(input("enter 1 or 2 "))
                            if choice6 == 2:
                                done = True

                            elif choice6 == 1:
                                done == False
                        postsleep()
                postsleep()
                        

                            
                            
                
