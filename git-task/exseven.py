import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "department": ["HR", "IT", "IT", "Finance", "HR"],
    "salary": [40000, 55000, 70000, 30000, 90000]
}
df = pd.DataFrame(data)
cutoff = df["salary"].quantile(0.75)
result = df[df["salary"] > cutoff]
print(result)
