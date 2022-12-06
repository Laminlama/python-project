import random

def get_tof_statements():

    statements=[]
    statements.append(["You only use 10 percent of your brain.", "F"])
    statements.append(["More than half of all pilots admit to sleeping on the job. ", "T"])
    statements.append(["Fifty percent of wealth on planet Earth is controlled by one percent of the population.", "T"])
    statements.append(["Humans share 60 percent of their DNA with bananas.", "T"])
    statements.append(["Fifteen percent of all daily Google searches have never been searched before. ", "T"])

    return statements 

def play_tof_quiz():

    # Get true or false statements 
    tof_statements = get_tof_statements()

    # Randomize tof statements
    random.shuffle(tof_statements)

    # Set player score to 0
    score = 0

    # Show tof statements using a loop
    for s in tof_statements:

        # present statement
        print("True or false: " + s[0])

        # user enter guess
        guess=input("Enter T or F: ")

        # check if guess is correct
        if guess == s[1]:
            print("Correct :)")
            # update score
            score = score+1
        else:
            print("Incorrect :(")
# Show final score
    print("Your final score is: "+str(score)+"\nThanks for playing!")

def main_menu():

    print("+------------------------------------------------------+")
    print("|Welcome to QUIZ                                       |")
    print("|made by Kshitij Singh , Sankalp Shakti and Lamin Lama!|")
    print("|Please select an option:                              |")
    print("|                                                      |")
    print("|1.Play True or False quiz                             |")
    print("|0.Quit                                                |")
    print("+------------------------------------------------------+")
    choice =input("Enter 1 or 0: ")
    if choice == "1":
        play_tof_quiz()
    elif choice == "0":
        print("Thanks for playing!")
        quit()

main_menu()