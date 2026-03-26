import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan","Feb","Mar","Apr"],
    "Profit": [1000,1500,1200,1800],
    "Facewash": [200,300,250,400],
    "Cream": [150,200,180,220]
}

df = pd.DataFrame(data)

plt.plot(df["Month"], df["Profit"])
plt.title("Profit Analysis")
plt.show()

plt.plot(df["Month"], df["Facewash"])
plt.plot(df["Month"], df["Cream"])
plt.title("Product Sales")
plt.show()


plt.bar(df["Month"], df["Facewash"])
plt.title("Facewash Sales")
plt.show()

plt.pie(df["Facewash"], labels=df["Month"], autopct='%1.1f%%')
plt.title("Sales Distribution")
plt.show()