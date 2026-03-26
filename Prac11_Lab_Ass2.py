import matplotlib.pyplot as plt

companies = ["Microsoft","Google","Amazon","IBM","Deloitte"]
recruitments = [50, 60, 55, 40, 45]

# Bar Chart
plt.bar(companies, recruitments)
plt.title("Recruitments")
plt.show()

# Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.show()

# Doughnut Chart
plt.pie(recruitments, labels=companies)
circle = plt.Circle((0,0), 0.5, color='white')
plt.gca().add_artist(circle)
plt.show()