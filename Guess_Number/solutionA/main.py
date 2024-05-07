import random

def validate_input(user,score):
    
    if not user.isdigit():
        print("Invalid input . please try again")
        return False

    user = int(user)
    if user > 100 or user < 1:
        print("Your guess is out of range! please try again.")
        score -= 5
        print(f"Your score is {score}!")
        return False
    return True


def display_menu():
    
    print("+" + "-" * 38 + "+")
    print("|" + " " * 38 + "|")
    print("|" + " " * 10 + "Welcome to the Game" + " " * 9 + "|")
    print("|" + " " * 38 + "|")
    print("|" + " " * 38 + "|")
    print("|" + "-" * 38 + "|")
    print("")
    print("     IF YOU WANNA QUITE GAME ETNER (q).")
    print("")



def main(): 
    
    score = 100
    number = random.randint(1,100)
    display_menu()

    while True:
        
        user_guess = input("Enter a number between 1 and 100: ")
        print("__________________________________")
        if user_guess == 'q':
            print("Thanks for choosing our platfrom to play. bye!")
            break
        
        if not validate_input(user_guess,score):
            continue
        user_guess = int(user_guess)
        if user_guess > number:
            print("Your guess is too high. Please try again. ")
        elif user_guess < number:
            print("Your guess is too low. Please try again. ")
        else:
            print("Congratulations! You guessed the correct number! ")
            print(f"Your score is {score}!")
            game = input("Do you wanna play again?(y/n) ")
            if game == 'y':
                score = 100
                number = random.randint(1,100)
                continue
            else:
                break
        score -= 10
        score = max(score,0)
    
            

if __name__ == "__main__":
    main()