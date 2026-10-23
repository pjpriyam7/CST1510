"""
RECORD CHECK  -  my version
===========================

Name  : Jhulloo Priyamvada
Lane  :  AI 
Date  : 21/10/2026

Run it:   python template.py
"""
# ======CLASS=======
# 1. Define a class called Record.
class Record:
    """Store one record and its threshold"""
    def __init__(self, dataset_name, rows_loaded, rows_expected):
        """Store dataset's 3 fields"""
        self.dataset_name= dataset_name
        self.rows_loaded= float(rows_loaded)
        self.rows_expected= float(rows_expected)
    def status(self):
        """Return dataset's threshold status"""
        if self.rows_loaded >= self.rows_expected:
            return "OVER LIMIT"
        elif self.rows_loaded >= self.rows_expected *0.90:
            return "WARNING"
        else:
            return "OK"

        
# ======RECORDS======
# 2. Create your records.
def load_records(path):
    """Load dataset records from a file"""
    records =[]
    try:
        with open(path, "r") as f:
            for line in f:
                dataset_name, rows_loaded, rows_expected = line.strip().split(",")    #Split each line into 3 fields
                record= Record(dataset_name, rows_loaded, rows_expected)
                records.append(record)
    except FileNotFoundError:
        print(f"File not found: {path}")
    return records
    
# ======OUTPUT======
# 3. Print a report for each record.
records= load_records("Week 05 - Classes and Objects/LAB/record1_sample.txt")
over_limit_count =0
for record in records:    # Calculate the status for record
    status = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.dataset_name}")
    print("=" * 34)
    print(f"Rows loaded:   {record.rows_loaded:g}")
    print(f"Rows expected: {record.rows_expected:g}")
    print(f"Status:        {status}")
    print("=" * 34)   
    if status == "OVER LIMIT":    #Count records that are over the limit
        over_limit_count+=1
print(f"\nTotal records OVER LIMIT: {over_limit_count}")  #Print final count after processing all records