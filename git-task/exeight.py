import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
    "category": ["A", "B", "A", "C", "B"],
    "sales": [100, 200, 150, 300, 250]
})
grouped = df.groupby("category")["sales"].sum()

grouped.plot(kind="bar")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Sales by Category")
plt.show()
