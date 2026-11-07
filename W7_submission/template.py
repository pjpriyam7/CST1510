"""
RECORD CHECK  -  my version
===========================

Name  : Jhulloo Priyamvada
Lane  :  AI 
Date  : 07/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

"""
RECORD CHECK - my version
===========================

Name  : Your name
Lane  : AI / Data Science
Date  : Your date

Run it: python template.py
"""
# ====== FUNCTIONS=====================
# 1. Clean and parse one survey record
def parse_line(raw_line):
    """Clean a survey record and return its data as a dictionary."""

    # Remove whitespace and convert the line to lowercase
    raw_line = raw_line.strip().lower()

    # Split the record into separate fields
    parts = raw_line.split(",")

    # Store the survey name in the dictionary
    data = {"survey": parts[0].strip()}

    # Extract and convert rating and age
    for part in parts[1:]:
        key, value = part.split("=", 1)
        # Clean the key and convert its value into an integer
        data[key.strip()] = int(value.strip())
    return data

# 2. Check whether survey rating should be flagged
def status_of(record):
    """Return FLAGGED for low ratings and OK for other ratings."""
    # Flag ratings of 2 or below.
    if record["rating"] <= 2:
        return "FLAGGED"
    else:
        return "OK"
# ======INPUT==============
# 3. Load raw survey records from text file
with open("raw_records.txt", "r") as f:
    raw_records = f.readlines()
# ======PROCESS + OUTPUT================
# 4. Parsing each record and display its status
total_records = 0
flagged_records = 0
for record in raw_records:
    # Clean the record using the parsing function
    data = parse_line(record)

    # Check the status of the survey.
    status = status_of(data)

    # Display the cleaned dictionary and its status
    print(data, "-", status)

    # Update the record counters
    total_records += 1
    if status == "FLAGGED":
        flagged_records += 1

# 5. Display a summary of the processed records
print("=======Summary=======")
print("Total records:", total_records)
print("Flagged records:", flagged_records)