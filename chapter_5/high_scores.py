# High Scores
# Demonstrates list methods

scores = []

choice = None
while choice != "0":

    print(
    """
    High Scores

    0 - Exit
    1 - Show Scores
    2 - Add a Score
    3 - Remove a Score
    4 - Sort Scores (low to high)
    5 - Sort Scores (high to low)
    """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # list high-score table
    elif choice == "1":
         print("High Scores")
         for score in scores:
            print(score)

    # add a score
    elif choice == "2":
        score = int(input("What score did you get?: "))
        scores.append(score)

    # remove a score
    elif choice == "3":
        score = int(input("Remove which score?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "isn't in the high scores list.")

    # sort scores low to high
    elif choice == "4":
        scores.sort(reverse=False)
        print(scores)

	# sort scores high to low
    elif choice == "5":
        scores.sort(reverse=True)
        print(scores)

    # some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")
