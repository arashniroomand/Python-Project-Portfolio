from src.utils.validate_input import get_valid_input
from src.game_logic.number_generator import generate_num
from src.game_logic.provide_hint import provide_hint
from src.game_logic.score import Score

def main():
    
    system_num = generate_num(1,100)
    score = Score()
    attempt = 0
    
    while True:
        user_guess , attempt = get_valid_input(1,100,attempt)
        if user_guess == system_num:
            print(f"You guess the number and you score is {score.get_score()}")
            print(f"You try {attempt} times to win! ")
            break
        else:
            hint = provide_hint(user_guess,system_num)
            print(hint)
            score.decrement_state()
            
    
    

if __name__ == '__main__':
    main()
    