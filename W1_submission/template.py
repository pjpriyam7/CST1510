"""
RECORD CHECK  -  my version
===========================

Name  : Jhulloo Priyamvada
Lane  :  AI   
Date  : 25/09/2026

Run it:   python template.py

"""

dataset_name = input("Enter dataset name: ")     
rows_loaded = int(input("Enter rows loaded: "))     
rows_expected = int(input("Enter rows expected: "))   
difference = rows_loaded- rows_expected
percent = (rows_loaded/rows_expected) *100  
print("")
print("=" * 34)
print(f"  RECORD CHECK  -  {dataset_name}")
print("=" * 34)
print(f"Loaded: {rows_loaded:10.2f}")
print(f"Expected: {rows_expected:10.2f}")
print(f"Difference: {difference:>+10.2f}")
print(f"Percent:{percent:>10.2f}%")
print("=" * 34)