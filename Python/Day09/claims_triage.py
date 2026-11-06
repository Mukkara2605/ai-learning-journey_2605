claims = [
    {"id": 1001, "amount": 250.00,  "status": "paid"},
    {"id": 1002, "amount": 0,       "status": "paid"},
    {"id": 1003, "amount": 1500.00, "status": "pending"},
    {"id": 1004, "amount": -40.00,  "status": "denied"},
    {"id": 1005, "amount": 980.50,  "status": "pending"},
    {"id": 1006, "amount": 2200.00, "status": "paid"},
]

category_counts = {}   # tally sheet, starts empty
valid_total = 0        # running total, starts at zero

for i, claim in enumerate(claims, start=1):
    claim_id = claim["id"]
    amount = claim["amount"]
    status = claim["status"]

    if amount <= 0:
        category = "invalid"
    elif amount >= 1000:
        category = "needs review"
    else:
        category = "auto-approve"

    print(f"{i}. Claim {claim_id} | ${amount:,.2f} | {category}")
    
    #Build a dict that counts how many claims fall in each category and print it.
    category_counts[category] = category_counts.get(category, 0) +1
    
    #Print the total amount of only the valid claims.
    
    if category != "invalid":
        valid_total += amount



print()
print(category_counts)
print(f"Total amount of valid amounts: ${valid_total:,.2f}")
