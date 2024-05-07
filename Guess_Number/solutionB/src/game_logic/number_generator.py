import random 

def generate_num(start:int,end:int) -> int:
    """Generate random number for the Guess number Game!"""
    random_num = random.randint(start,end)
    return random_num

        