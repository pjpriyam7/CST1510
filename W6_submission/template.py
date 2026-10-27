"""
RECORD CHECK  -  my version
===========================

Name  : Jhulloo Priyamvada
Lane  :  AI
Date  : 27/10/2026

Run it:   python template.py

"""

"""Reads AI dataset information from CSV file. Calculates the percentage of rows loaded, assigns a status to each dataset, displays results, saves a report
and creates a bar chart showing the number of datasets per status"""

import pandas as pd
import matplotlib.pyplot as plt
#============ LOAD ================
# Read the CSV file into a DataFrame
df = pd.read_csv("ai_datasets.csv")

# ================== PROCESS=======================
# Percent of expected rows that were actually loaded
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else ("WARNING" if p >= 90 else "OK")
)
# ========OUTPUT=========
# 3. Print the DataFrame.
print(df)                                    #the full table, including percent and status
print(df[df["status"] != "OK"])              #only the rows that are not OK
#count how many datasets are in each status group
status_counts = df["status"].value_counts()
print(status_counts)

df.to_csv("ai_datasets_report.csv", index=False)      #Saving the full table to a new CSV

# Bar chart of the counts
status_counts.plot(kind="bar")
plt.title("Datasets per status")
plt.savefig("ai_status_counts.png")
plt.show()