import pandas as pd

df = pd.DataFrame({
    "cut": ["Ideal","Premium","Good","Premium","Good"],
    "price": [326,326,327,334,335],
    "x": [3.95,3.89,4.05,4.20,4.34],
    "y": [3.98,3.84,4.07,4.23,4.35],
    "z": [2.43,2.31,2.31,2.63,2.75]
})

print(df.groupby("cut")["price"].mean())

print("Count:", df["price"].count())
print("Min:", df["price"].min())
print("Max:", df["price"].max())

print("Avg x:", df["x"].mean())
print("Avg y:", df["y"].mean())
print("Avg z:", df["z"].mean())