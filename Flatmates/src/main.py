from colorama import Fore, Style, init
from info import *
from menu import *

init(autoreset=True)  # Enable auto reset of color after each print


def main():
    while True:
        print_welcome()

        amount = get_float("💰 Enter the total bill amount: ")
        period = input("🗓️ Enter the bill period (e.g., June 2025): ")

        print(Fore.MAGENTA + "\nNow enter information for the flatmates:")
        person1 = collect_flatmate_info(1)
        person2 = collect_flatmate_info(2)

        bill = Bill(amount, period)

        show_result_and_generate_pdf(person1, person2, bill)

        again = input("\nDo you want to calculate another bill? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print(Fore.CYAN + "👋 Goodbye! Thanks for using the app.")
            break


if __name__ == "__main__":
    main()


    