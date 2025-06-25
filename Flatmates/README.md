# 🏠 Flatmates Bill Splitter App

A simple Python CLI app that helps flatmates fairly split the cost of a shared bill based on how many days each person stayed in the house during a billing period.

---

## 📂 Project Structure
```
flatmates-bill-splitter/
│
├── src/
│ ├── main.py # Entry point with CLI logic and menu
│ ├── flat.py # Contains Bill and Flatmate classes and their logic
│ ├── reports.py # Generates a PDF report of the bill split
│ ├── info.py # Contains constants like the PDF output path
│ └── menu.py #
│
├── files/
│ ├── Flatmates_Report.pdf # Output report PDF (auto-generated)
│ └── house.png # Image used in the PDF report 
│
├── README.md # Project documentation (you're reading it!)
└── requirements.txt # List of required libraries 
```

---

## 🚀 How to Run

### 1. **Clone the repository:**

```bash
git clone https://github.com/your-username/flatmates-bill-splitter.git
cd flatmates-bill-splitter/src
```

## Install dependencies:
```
pip install -r ../requirements.txt
```

### Example:
```
Hey user, enter the bill amount: 120
What is the bill period? E.g. December 2020: June 2025

What is the name of flatmate 1? Alice
How many days did Alice stay in the house? 20

What is the name of flatmate 2? Bob
How many days did Bob stay in the house? 10

Alice pays: $80.0
Bob pays: $40.0
✅ PDF report generated successfully!
```