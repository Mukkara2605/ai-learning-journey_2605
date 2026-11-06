"""
    Assignment 3: Four one-line comprehensions

File: comprehensions_practice.py

python
amounts = [120, 0, 560, -5, 90, 1500]
claims = [
    {"id": 1001, "amount": 250,  "status": "paid"},
    {"id": 1002, "amount": 900,  "status": "denied"},
    {"id": 1003, "amount": 1500, "status": "paid"},
    {"id": 1004, "amount": 75,   "status": "pending"},
]

Write each as one comprehension:

A list of only the positive amounts.
A list of positive amounts with 10% added, rounded to 2 decimals.
A dict mapping claim id to amount, for paid claims only.
A set of the unique statuses.

"""
amounts = [120, 0, 560, -5, 90, 1500]
claims = [
    {"id": 1001, "amount": 250,  "status": "paid"},
    {"id": 1002, "amount": 900,  "status": "denied"},
    {"id": 1003, "amount": 1500, "status": "paid"},
    {"id": 1004, "amount": 75,   "status": "pending"},
]
# Positive amounts 
positive_amounts = [amount for amount in amounts if amount >0]

# Positive amounts with 10% added, rounded to 2 decimals
positive_amounts_with_10_percent = [round(amount * 1.1, 2) for amount in amounts if amount > 0]

# Dict mapping claim id to amount, for paid claims only
paid_claims_dict = {claim["id"]: claim["amount"] for claim in claims if claim["status"] == "paid"}

# Set of the unique statuses
unique_statuses = {claim["status"] for claim in claims}

print("Positive amounts:", positive_amounts)
print("Positive amounts with 10% added:", positive_amounts_with_10_percent)
print("Paid claims dict:", paid_claims_dict)
print("Unique statuses:", unique_statuses)

