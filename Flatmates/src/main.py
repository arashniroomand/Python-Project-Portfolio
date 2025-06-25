from flat import Bill, Flatmate
from reports import PdfReport
from info import *
from colorama import Fore, Style, init

init(autoreset=True)  # Enable auto reset of color after each print

def print_welcome():
    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + "🏠 Welcome to Flatmates Bill Splitter App 🧾")
    print(Fore.CYAN + "=" * 50)


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "Please enter a valid number!")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(Fore.RED + "Please enter a valid integer!")


def collect_flatmate_info(num):
    name = input(f"What is the name of flatmate {num}? ")
    days = get_int(f"How many days did {name} stay in the house? ")
    return Flatmate(name, days)


def show_result_and_generate_pdf(person1, person2, bill):
    print(Fore.YELLOW + f"\n{person1.name} pays: ${round(person1.pays(bill, person2), 2)}")
    print(Fore.YELLOW + f"{person2.name} pays: ${round(person2.pays(bill, person1), 2)}")

    choice = input("\nDo you want to generate a PDF report? (yes/no): ").lower()
    if choice in ["yes", "y"]:
        pdf_report = PdfReport(FILE_PATH)
        pdf_report.generate(person1, person2, bill)
        print(Fore.GREEN + "✅ PDF report generated successfully!")
    else:
        print(Fore.BLUE + "Skipping PDF report generation.")

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


    