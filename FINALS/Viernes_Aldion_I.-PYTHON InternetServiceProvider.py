class InternetPlan:
    def __init__(self, name, price, bandwidth_limit, excess_rate):
        self.name = name
        self.price = price
        self.bandwidth_limit = bandwidth_limit
        self.excess_rate = excess_rate

    def calculate_bill(self, bandwidth_consumed):
        regular_amount = self.price
        if bandwidth_consumed > self.bandwidth_limit:
            excess_bandwidth = bandwidth_consumed - self.bandwidth_limit
            excess_amount = excess_bandwidth * self.excess_rate
            total_amount = regular_amount + excess_amount
        else:
            total_amount = regular_amount

        return total_amount

    def display_receipt(self, customer_info, bandwidth_consumed):
        print("Receipt:")
        print("Name:", customer_info['name'])
        print("Account Number:", customer_info['account_number'])
        print("Phone Number:", customer_info['phone_number'])
        print("Email Address:", customer_info['email_address'])
        print("Internet Plan:", self.name)
        print(f"Bandwidth Consumed: {bandwidth_consumed // 1024} GB and {bandwidth_consumed % 1024} MB")
        print("Total Amount: PHP", self.calculate_bill(bandwidth_consumed))


def get_customer_info():
    customer_info = {}
    customer_info['name'] = input("Enter the name of the customer: ")
    customer_info['account_number'] = input("Enter the account number of the customer: ")
    customer_info['phone_number'] = input("Enter the phone number of the customer: ")
    customer_info['email_address'] = input("Enter the email address of the customer: ")
    customer_info['internet_plan'] = input("Enter the internet plan of the customer (Standard, Pro, or Business): ")
    customer_info['bandwidth_consumed'] = int(input("Enter the bandwidth consumed by the customer (in MB): "))
    return customer_info


standard_plan = InternetPlan("Standard", 1000, 30 * 1024, 0.05)
pro_plan = InternetPlan("Pro", 2000, 60 * 1024, 0.15)
business_plan = InternetPlan("Business", 3500, 120 * 1024, 0.5)

customer_info = get_customer_info()

if customer_info['internet_plan'] == "Standard":
    plan = standard_plan
elif customer_info['internet_plan'] == "Pro":
    plan = pro_plan
elif customer_info['internet_plan'] == "Business":
    plan = business_plan
else:
    print("Invalid internet plan. Please choose Standard, Pro, or Business.")
    exit()

plan.display_receipt(customer_info, customer_info['bandwidth_consumed'])