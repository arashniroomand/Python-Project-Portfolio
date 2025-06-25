from flat import Bill, Flatmate
from reports import PdfReport
from info import *


if __name__ == '__main__':
    amount = float(input("Hey user, enter the bill amount: "))
    period = input("What is the bill period? E.g. December 2020: ")
    
    name1 = input("What is faltmate1: ")
    days_in_house1 = int(input(f"How many days did {name1} stay in the houst during the bill period? "))
    
    name2 = input("What is flatmate2: ")
    days_in_house2 = int(input(f"How many days did {name2} stay in the houst during the bill period? "))
    
    bill = Bill(amount, period)
    person1 = Flatmate(name1, days_in_house1)
    person2 = Flatmate(name2, days_in_house2)
    print(f"{person1.name} pays: ", round(person1.pays(bill, person2), 2))
    print(f"{person2.name} pays: ", round(person2.pays(bill, person1), 2))

    pdf_report = PdfReport(FILE_PATH)
    pdf_report_generate = pdf_report.generate(person1, person2, bill)



    