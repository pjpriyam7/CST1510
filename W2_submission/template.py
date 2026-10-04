"""
RECORD CHECK  -  my version
===========================

Name  : Priyamvada Jhulloo
Lane  :  AI
Date  : 1st Oct 2026

Run it:   python template.py
"""
over_limit=0
while True:
# 1. Ask for your three values.
    dataset_name= input("Enter dataset name(or quit to stop): ")
    if dataset_name == "quit":
        break
    rows_loaded= float(input("Enter the rows loaded: "))
    rows_expected= float(input("Enter the rows expected: "))
#2. Work out the difference and the percentage
    difference = rows_expected-rows_loaded
    percent =(rows_loaded/rows_expected)*100

#3. Decide a status and store it in a variable called status
    if percent >= 100:
        status= "OVER LIMIT"
        over_limit += 1
    elif percent >= 90:
        status= "WARNING"
    else:
        status = "OK"
    
# 4. Print the report.
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {dataset_name}")
    print("=" * 34)
    print(f"Used    : {rows_loaded:>8.2f}")
    print(f"Total   : {rows_expected:>8.2f}")
    print(f"Free    : {difference:>8.2f}")
    print(f"Percent : {percent:>8.2f}%")
    print(f"Status  : {status}")
    print("=" * 34)
# Print the count once after the loop
print(f"OVER LIMIT record: ", over_limit)

#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.