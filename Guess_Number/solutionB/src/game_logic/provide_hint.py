def provide_hint(user_guess,system_guess):
    """provide a hint"""
    
    if user_guess > system_guess:
        return "Your guess is higher than the number!"
    else:
        return "Your Guess is lower than the number!"
    