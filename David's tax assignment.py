def calculate_tax(status, income):
    brackets = {
        0: [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)],
        1: [(16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)],
        2: [(8350, 0.10), (33950, 0.15), (68525, 0.25), (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)],
        3: [(11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)]
    }
    
    tax = 0.0
    prev_limit = 0
    for limit, rate in brackets[status]:
        taxable = min(income, limit) - prev_limit
        if taxable > 0:
            tax += taxable * rate
        prev_limit = limit
        if income <= limit:
            break
    return tax

def main():
    try:
        status = int(input("Enter filing status (0=Single, 1=Married Joint/QW, 2=Married Separate, 3=Head of Household): "))
        income = float(input("Enter taxable income: "))
        if status not in range(4):
            print("Invalid filing status.")
            return
        tax = calculate_tax(status, income)
        print(f"Total tax: ${tax:.2f}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()