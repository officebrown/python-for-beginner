# Mood Computer
# Demonstrates the elif clause

import random

print("I sense your energy.  Your true emotions are coming across my screen.")
print("You are...")

#mood = random.randint(1, 3)
entry = input("enter your mood: from 1(happy) to 3(sad): ")
mood = int(entry)

if mood == 1:
    # happy
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       -----------
                   """)
elif mood == 2:
    # neutral
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | ------  |
       |         |
       -----------
                   """)
elif mood == 3:
    # sad
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       |  .'.    |
       | '   '   |
       -----------
                   """)
else:
    print("Illegal mood value!  (You must be in a really bad mood).")

print("...today.")

input("\n\nPress the enter key to exit.")
