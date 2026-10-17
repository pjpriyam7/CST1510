"""
RECORD CHECK  -  my version
===========================

Name  : Jhulloo Priyamvada
Lane  :  AI 
Date  : 15/10/2026

Run it:   python template.py

"""
# =====FUNCTIONS=======
#1. Return status based on percentage
def status_of(percent):
    """ Return status based on percentage"""
    if percent>= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    
#2. Calculate the difference and percentage
def check(rows_loaded,rows_expected):
    """Return missing rows and percentage loaded"""
    rows_missing= rows_expected-rows_loaded
    percent_loaded= (rows_loaded/rows_expected)*100
    return rows_missing,percent_loaded

#3. Print complete report for one dataset
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

# =====STORE=====

def load_records(path):
    """Load dataset records from file"""
    records=[]
    #open file and read each line
    with open(path,"r") as f:
        for line in f:
            dataset_name, rows_loaded, rows_expected = line.strip().split(",")
            rows_loaded= float(rows_loaded)
            rows_expected= float(rows_expected)
            records.append({
                "dataset_name": dataset_name,
                "rows_loaded": rows_loaded,
                "rows_expected": rows_expected
            })
    return records
#Try to load records from file

# ===== STORE =====
try:
    records = load_records("Week 04 - Lists, Dictionaries and Files\LAB\datasets.txt")

except FileNotFoundError:
    print("File not found:","datasets.txt") 
    records = []

# =====PROCESS + OUTPUT======

over_limit = 0
with open("results.txt","w") as f:
    for i in records:
        dataset_name=i["dataset_name"]
        rows_loaded=i["rows_loaded"]
        rows_expected= i['rows_expected']

        rows_missing, percent_loaded = check(rows_loaded,rows_expected)
        status= status_of(percent_loaded)
        print_report(
            dataset_name, rows_loaded, rows_expected, rows_missing, percent_loaded, status
        )
        f.write(dataset_name + "," + status + "\n")

        #   Count datasets over limit
        if status == "OVER LIMIT":
            over_limit += 1

print()
print("="*34)
print(f"Datasets over limit: {over_limit}")
print("="*34)