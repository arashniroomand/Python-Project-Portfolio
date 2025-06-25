from fpdf import FPDF
import webbrowser

from info import IMAGE_PATH


class PdfReport:
    """
    Creates a pdf file that write a report of the deal
    """
    
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self,  flatmate1, flatmate2, bill):
        pdf = FPDF(orientation = 'P', unit = 'pt', format = 'A5')
        pdf.add_page()
        
        # Add image
        pdf.image(IMAGE_PATH, w = 100, h = 100)
        
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
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
        