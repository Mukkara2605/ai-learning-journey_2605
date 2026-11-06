"""
Assignment 4: ID reconciliation as a function (sets + functions)

File: reconcile_ids.py

Write a function reconcile(source_ids, target_ids) that returns a dict with these keys: missing_in_target, extra_in_target, matched_count, and result ("PASS" only if there are no missing and no extra IDs, otherwise "FAIL").

Test it with:

python
source = [101, 102, 103, 104, 105, 105]   # note the duplicate
target = [101, 103, 104, 106]

Tasks:

Make the function handle duplicates (convert to sets first).
Print the result nicely with f-strings. Show sorted lists for missing and extra.
Test a second case that should print PASS.
Add one line that prints the match rate as a percentage, e.g. Match rate: 60.0% (matched ÷ unique source IDs).
"""


def reconcile(source_ids, target_ids):
    # Convert to sets to handle duplicates
    source_set = set(source_ids)
    target_set = set(target_ids)

    # Find missing and extra IDs
    missing_in_target = sorted(source_set - target_set)
    extra_in_target = sorted(target_set - source_set)

    # Calculate matched count
    matched_count = len(source_set & target_set)

    # Calculate match rate
    unique_source_ids = len(source_set)
    match_rate = (matched_count / unique_source_ids * 100) if unique_source_ids > 0 else 0

    # Determine result
    if not missing_in_target and not extra_in_target:
        result = "PASS"
    else:
        result = "FAIL"

    # Print the result nicely
    print(f"Result: {result}")
    print(f"Missing in target: {missing_in_target}")
    print(f"Extra in target: {extra_in_target}")
    print(f"Matched count: {matched_count}")
    print(f"Match rate: {match_rate:.1f}% (matched ÷ unique source IDs)")

    return {
        "missing_in_target": missing_in_target,
        "extra_in_target": extra_in_target,
        "matched_count": matched_count,
        "result": result
    }

# Test with the provided example
source = [101, 102, 103, 104, 105, 105]
target = [101, 103, 104, 106]
reconcile(source, target)

# Test a second case that should print PASS
source2 = [101, 102, 103]
target2 = [101, 102, 103]
reconcile(source2, target2)