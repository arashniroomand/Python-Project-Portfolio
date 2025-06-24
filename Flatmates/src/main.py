from fpdf import FPDF
import webbrowser

from info import FILE_PATH

class Bill:
    """
    Object that contains data about a bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
        

class Flatmate:
    """
    Creates a flatmate person who lives in a flat
    and pays a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay
    

class PdfReport:
    """
    Creates a pdf file that write a report of the deal
    """
    
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self,  flatmate1, flatmate2, bill):
        pdf = FPDF(orientation = 'P', unit = 'pt', format = 'A5')
        pdf.add_page()
        
        flatmate1_pay = str(round(flatmate1.pays(bill, person2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, person1), 2))
        # Insert title
        pdf.set_font(family = 'Times', size = 24, style = 'B')
        pdf.cell(w = 0, h = 80, txt = "Flatmates Bill", border = 1, align = "C", ln =1) 
        # Insert Period Labels
        pdf.set_font(family = 'Times', size = 14, style = 'B')
        pdf.cell(w = 100, h = 40, txt = "Period: ", border = 0)
        pdf.cell(w = 200, h = 40, txt = bill.period, border = 0, ln =1)
        
        # insert name and due amount of the first flatmate
        pdf.set_font(family = 'Times', size = 12, style = 'B')
        pdf.cell(w = 100, h = 20, txt = str(flatmate1.name), border = 0)
        pdf.cell(w = 200, h = 20, txt = flatmate1_pay, border = 0, ln =1)
        
        pdf.cell(w = 100, h = 20, txt = str(flatmate2.name), border = 0)
        pdf.cell(w = 200, h = 20, txt = flatmate2_pay, border = 0, ln =1)
        
        pdf.output(self.filename)
        webbrowser.open(self.filename)
        


if __name__ == '__main__':
    bill = Bill(120, 'March 21')
    person1 = Flatmate("arash", 25)
    person2 = Flatmate("shiva", 20)
    print(f"{person1.name} pays: ", round(person1.pays(bill, person2), 2))
    print(f"{person2.name} pays: ", round(person2.pays(bill, person1), 2))

    pdf_report = PdfReport(FILE_PATH)
    pdf_report_generate = pdf_report.generate(person1, person2, bill)



    