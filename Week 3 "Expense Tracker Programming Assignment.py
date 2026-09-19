#Programming Assignment: Personal Expense Tracker
# Author: Arshpreet Kandola
# Date: September 17, 2026
# Description: A program that saves and displays personal expenses
# Tier Level: Base

import os
import datetime

# Builds an expense record
def build_record(description, amount, category):
    date = str(datetime.date.today())
    description = description[:30]
    amount = f"{amount:.2f}"

    record = ",".join([date, description, amount, category])
    return record


# Loads records 
def load_records(filename):
    records = []

    try:
        file = open(filename, "r")

        for line in file:
            line = line.strip()

            if line != "":
                record = line.split(",")
                records.append(record)

        file.close()

    except FileNotFoundError:
        return []

    return records


# Save a record
def save_record(filename, record):
    file = open(filename, "a")
    file.write(record + "\n")
    file.close()


# Displays the records
def display_records(records):
    if len(records) == 0:
        print("No expenses on record yet.")
    else:
        print(f"{'Date':<12}{'Description':<32}{'Amount':<10}{'Category':<15}")
        print("-" * 69)

        for record in records:
            print(f"{record[0]:<12}{record[1]:<32}${record[2]:<10}{record[3]:<15}")


# Main program
filename = "Arsh's fun expenses.txt"

print("=====Arsh Kandola's Expense Records =====")

records = load_records(filename)
display_records(records)

number = int(input("How many things you wanna spend on? "))

for i in range(number):
    print(f"\n--- Expense {i + 1} ---")

    description = input("Description: ")
    amount = float(input("Amount: "))
    category = input("Category: ")

    record = build_record(description, amount, category)
    save_record(filename, record)

print("\n===== Updated Expense Records =====")

records = load_records(filename)
display_records(records)