"""
RECORD CHECK  -  my version
===========================

Name  : Jhulloo Priyamvada
Lane  : AI   
Date  : 08/10/2026

Run it:   python template.py

"""

# FUNCTIONS
def status_of(percent):
    """ Return status based on percentage"""
    if percent>= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    
def check(rows_loaded,rows_expected):
    """Return missing rows and percentage loaded"""
    missing_rows= rows_expected-rows_loaded   #calculate number of rows missing from expected number of rows
    percent= (rows_loaded/rows_expected)*100  #Calculate percentage of rows successfully loaded
    return missing_rows,percent

def print_report(dataset_name, rows_loaded,rows_expected,rows_missing,percent_loaded, status):
    """Print a report for one dataset"""
    #Printing header section
    print()
    print("="*34)
    print(f" DATASET CHECK- {dataset_name}")
    print("="*34)

#Print formatted metrics right-aligned to 10 spaces with 2 d.p

    print(f"Rows loaded    :   {rows_loaded:>10.2f}")
    print(f"Rows expected  :   {rows_expected:>10.2f}")
    print(f"Rows missing   :   {rows_missing:>10.2f}")
    print(f"Percent loaded :   {percent_loaded:>10.2f}%")
    print(f"Status         :   {status}")
    print("="*34)

#INPUT
over_limit_count= 0
while True:
    #Get dataset name or exit command from user
    dataset_name= input(" Enter dataset name(or 'quit' to stop): ")
    if dataset_name == "quit":
        break #Exit loop immediately

    #Get numerical row count inputs
    rows_loaded= float(input("Enter rows loaded: "))
    rows_expected= float(input("Enter rows expected: "))

# PROCESS- calculate missing rows and percentage loaded
    rows_missing, percent_loaded= check(rows_loaded,rows_expected)
    status= status_of(percent_loaded)  #Determine status based on percentage
# OUTPUT
    print_report(dataset_name,rows_loaded,rows_expected,rows_missing, percent_loaded, status)

    #Count how many datasets exceed the limit
    if status == "OVER LIMIT":
        over_limit_count +=1

print()
print("=" * 34)
print(f"Datasets over limit:  {over_limit_count}")
print("="*34)