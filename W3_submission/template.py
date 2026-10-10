"""
RECORD CHECK  -  my version
===========================

Name  : Jhulloo Priyamvada
Lane  : AI   
Date  : 08/10/2026

Run it:   python template.py

"""

# FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).

def status_of(percent):
    """ Return status based on percentage"""
    if percent>= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.

def check(value,limit):
    """Return missing rows and percentage loaded"""
    difference= limit-value
    percent= (value/limit)*100
    return difference,percent

#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.

def print_report(dataset_name, rows_loaded,rows_expected,rows_missing,percent_loaded, status):
    """Print a report for one dataset"""
    print()
    print("="*34)
    print(f" DATASET CHECK- {dataset_name}")
    print("="*34)
    print(f"Rows loaded   :   {rows_loaded:>10.2f}")
    print(f"Rows expected :   {rows_expected:>10.2f}")
    print(f"Rows missing  :   {rows_missing:>10.2f}")
    print(f"Percent loaded:   {percent_loaded:>10.2f}%")
    print(f"Status        :   {status}")
    print("="*34)

#INPUT
over_limit_count= 0
while True:
    dataset_name= input(" Enter dataset name(or 'quit' to stop): ")
    if dataset_name == "quit":
        break
    rows_loaded= float(input("Enter rows loaded: "))
    rows_expected= float(input("Enter rows expected: "))
# PROCESS
    rows_missing, percent_loaded= check(rows_loaded,rows_expected)
    status= status_of(percent_loaded)
# OUTPUT
    print_report(dataset_name,rows_loaded,rows_expected,rows_missing, percent_loaded, status)
    if status == "OVER LIMIT":
        over_limit_count +=1

print()
print("=" * 34)
print(f"Datasets over limit:  {over_limit_count}")
print("="*34)




#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.
# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
