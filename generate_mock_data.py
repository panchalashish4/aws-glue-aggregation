import csv
from datetime import date, timedelta
from random import randint, choice

# Define customer and bank names
customer_names = ["John Doe", "Jane Smith", "Michael Brown", "Sarah Lee", "David Miller"]
bank_names = ["Citibank", "Chase", "Bank of America", "Wells Fargo", "PNC"]

# Define debit card types
card_types = ["Visa", "Mastercard"]

# Define number of customers and transactions per day
num_customers = 10
transactions_per_customer = 3


def generate_transaction(customer_id):
    """Generates a mock transaction record"""
    name = choice(customer_names)
    card_number = f"{randint(1000, 9999)}-{randint(1000, 9999)}-{randint(1000, 9999)}-{randint(1000, 9999)}"
    card_type = choice(card_types)
    bank_name = choice(bank_names)
    transaction_date = str(date.today())
    amount = round(randint(10, 100) + randint(0, 99) / 100, 2)  # Up to 2 decimal places
    return [customer_id, name, card_number, card_type, bank_name, transaction_date, amount]


def generate_transactions(customer_id_start, customer_id_end, num_transactions):
    """Generates a list of mock transaction records"""
    transactions = []
    for i in range(customer_id_start, customer_id_end + 1):
        for _ in range(num_transactions):
            transactions.append(generate_transaction(i))
    return transactions


def write_to_csv(data, filename):
    """Writes data to a CSV file"""
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["customer_id", "name", "debit_card_number", "debit_card_type", "bank_name", "transaction_date",
                         "amount_spend"])
        writer.writerows(data)
    return


def generate_data(start_date, end_date, date_str):
    """Generates data and creates csv files"""
    transactions = generate_transactions(1, num_customers, transactions_per_customer)
    write_to_csv(transactions, f"/tmp/transactions_{date_str}.csv")

    print(f"Generated mock transaction data transactions_{date_str}.csv and saved in csv files")
    return
