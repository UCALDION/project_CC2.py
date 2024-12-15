def calculate_payroll():
    def get_name_input(name):
        name = input(name)
        return name

    def get_name_input(name):
        print("--------------------------------------------------------------------------------")
        print("Welcome to the Ere Bank of the Philippines Payroll System!")
        print("Please enter your employee information below:")
        print("--------------------------------------------------------------------------------")
        name = input(name)
        return name
    
    def get_id_number_input():
        while True:
            try:
                id_number = int(input("Enter your 6 digits ID number: "))
                if 100000 <= id_number <= 999999:
                    return id_number
                else:
                    print("Invalid input. Please enter a valid 6-digit ID number.")
            except ValueError:
                print("Invalid input. Please enter a valid 6-digit ID number.")

    def get_income_input():
        while True:
            try:
                income = float(input("Enter your gross monthly income: "))
                if income >= 0:
                    return income
                else:
                    print("Please enter a valid gross monthly income.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_tax_amount(income, tax_rate):
        return income * tax_rate

    def get_tax_rate(income):
        if income <= 14999:
           return 0.10
        elif income <= 39999:
           return 0.14
        elif income <= 99999:
           return 0.18
        else:
           return 0.26

    def get_contribution(income):
        if income <= 14999:
            return 300
        elif income <= 39999:
            return 600
        elif income <= 99999:
            return 900
        else:
            return 1200

    def get_health_contribution(income):
        if income <= 14999:
            return 150
        elif income <= 39999:
            return 300
        elif income <= 99999:
            return 450
        else:
            return 600
    
    def print_payroll_info(name, id_number, tax_amount, sss_gsis, phil_health, net_income):
        print("--------------------------------------------------------------------------------")
        print(f"Employee Name: = {name}")
        print(f"Employee ID Number: = {id_number:06}")
        print(f"Income Tax: = PHP {tax_amount: .2f}")
        print(f"SSS/GSIS Contribution: = PHP {sss_gsis: .2f}")
        print(f"Phil Health Contribution: = PHP {phil_health: .2f}")
        print(f"Gross Monthly Income: = PHP {income: .2f}")
        print(f"Net Monthly Income: = PHP {net_income: .2f}")
        print("--------------------------------------------------------------------------------")

    name = get_name_input("Please enter your Full Name: ")
    id_number = get_id_number_input()
    income = get_income_input()

    sss_gsis = get_contribution(income)
    phil_health = get_health_contribution(income)

    tax_rate = get_tax_rate(income)
    tax_amount = income * tax_rate

    net_income = income - sss_gsis - phil_health - tax_amount

    print_payroll_info(name, id_number, tax_amount, sss_gsis, phil_health, net_income)

if __name__ == '__main__':
    calculate_payroll()
    
