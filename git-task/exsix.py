import pandas as pd

C = pd.Series([25, 30, 15, 40], index=['Mon', 'Tue', 'Wed', 'Thu'])
F = C * 9/5 + 32

print("Celsius:\n", C)
print("\nFahrenheit:\n", F)
