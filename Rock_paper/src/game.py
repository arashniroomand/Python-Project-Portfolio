"""
Author : Arash Niroumand
Date : 2024
Description : Rock Paper Scissors game
"""

import random
from typing import List , Tuple , Dict

class RockPaperScissors:
    """Rock Papaer Scissors class"""
    
    def __init__(self,name: str):
        self.choice = ['rock','paper','scissors']
        self.name = name
        
    def get_player_choice(self):
        player_choice = input(f"Enter your choice dear {self.name} : ")
        if player_choice.lower() in self.choice:
            return player_choice
        else:
            print(f"Invalid choice! options include {self.choice} ")
            check = input("Do you want to try again? (y/n) : ")
            if check.lower() in ['y','yes']:
                return self.get_player_choice()
            else:
                print("Thank you for playing!")

    
    def get_computer_choice(self):
        """ Get computer choice randomly"""
        return random.choice(self.choice)
    
    def get_winner(self,player_choice,computer_choice):
        """ We get the player choice and chek it with computer choice to find the winner of the game."""
        if player_choice == computer_choice:
            return "It's tie!"
        
        win_combinations = [('rock','scissors'),('paper','rock'),('scissors','paper')]
        for win_combin in win_combinations:
            if player_choice == win_combin[0] and computer_choice == win_combin[1]:
                return f"Congrats! You won! {player_choice} beats {computer_choice}"
        return "Oh no! the computer win the game :)))"
    
    def play(self):
        """- Get your choice
        - Get computer choice
        - Decide the winner
        - Print the result and see the winner!
        """
        user_choice = self.get_player_choice()
        computer = self.get_computer_choice()
        winner = self.get_winner(user_choice,computer)
        print(winner)
        print(f"Your choice was {user_choice} and computer choice was {computer}")
        repeat = input("Do you wanna play again? (y/n) : ")
        if repeat in ['y','yes']:
            self.play()
        else:
            print()
            print('*'*22)
            print("Thank you for playing!")
            print('*'*22)

if __name__ == '__main__':      
    player1 = RockPaperScissors('arash')
    player1.play()