import pandas as pd

df = pd.read_excel("employee.xlsx")

print("Automotive Employees:")
print(df[df["Department"] == "Automotive"])

eid = int(input("\nEnter Employee ID: "))
print("\nEmployee Details:")
print(df[df["Employee ID"] == eid])

print("\nDevelopers List:")
print(df[df["Designation"] == "Developer"])