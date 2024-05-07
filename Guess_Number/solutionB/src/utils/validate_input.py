
def get_valid_input(start,end,attempt):
    while True:
        try:
            user_guess = int(input(f"Enter a number between {start} and {end}: "))
            attempt += 1
            if user_guess > end or user_guess < start:
                print("Your number is out of range ... try again")
                continue
            return user_guess,attempt
        except:
            print("Invalid input... please follow the rules! ")
            continue
        
        
