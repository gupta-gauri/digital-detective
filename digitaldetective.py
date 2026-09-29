# Digital Detective
# Case: Missing Laptop

print("DIGITAL DETECTIVE- MISSING LAPTOP CASE")

# Information about suspects
suspects = {
    "1": "Aarav",
    "2": "Riya",
    "3": "Kabir"
}

# Some clues
clues = [
    "The laptop was kept on Table 7.",
    "The CCTV stopped working at 2:10 PM.",
    "Kabir entered the lab at 2:05 PM.",
    "Aarav was in the library at that time."
]

score = 0

while True:

    print("\n------ MENU ------")
    print("1. See suspects")
    print("2. See clues")
    print("3. Question a suspect")
    print("4. Make accusation")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nSuspects:")
        print("1. Aarav - Lab Assistant")
        print("2. Riya - Student")
        print("3. Kabir - Student")

    elif choice == "2":

        print("\nClues:")

        for clue in clues:
            print("-", clue)

        score = score + 10
        print("\nYou found a clue!")
        print("Score:", score)

    elif choice == "3":

        print("\nWho do you want to question?")
        print("1. Aarav")
        print("2. Riya")
        print("3. Kabir")

        suspect = input("Enter number: ")

        if suspect == "1":
            print("\nAarav says:")
            print("I was in the library arranging books.")

        elif suspect == "2":
            print("\nRiya says:")
            print("I was attending my lecture.")

        elif suspect == "3":
            print("\nKabir says:")
            print("I was working on my project in the computer lab.")
            print("But the timing of his statement needs to be checked.")

        else:
            print("Wrong choice.")

    elif choice == "4":

        print("\nWho do you think took the laptop?")
        print("1. Aarav")
        print("2. Riya")
        print("3. Kabir")

        answer = input("Enter your answer: ")

        if answer == "3":
            print("\nYour answer matches the clues.")
            print("Kabir was in the lab when the laptop disappeared.")
            score = score + 50
            print("Final Score:", score)

        elif answer == "1" or answer == "2":
            print("\nThis answer does not match the clues.")
            print("Try checking the evidence again.")

        else:
            print("Wrong choice.")

    elif choice == "5":

        print("\nInvestigation finished.")
        print("Your score:", score)
        print("Thank you for playing!")

        break

    else:
        print("\nPlease enter a number from 1 to 5.")