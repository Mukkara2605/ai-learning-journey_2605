# Time splitter (time_split.py): ask for total minutes and print hours and minutes, using // and %.

Total_min = int(input("Enter minutes: "))
hrs = Total_min // 60
min = Total_min % 60
print(f"{Total_min} minutes is equal to {hrs} hours and {min} minutes.")