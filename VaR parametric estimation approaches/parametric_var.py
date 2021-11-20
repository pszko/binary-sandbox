# python program to demonstrate parametric normal VaR

import pandas as pd
import numpy as np

df = pd.read_csv('SPY.csv', index_col='date', sep=',', encoding='utf-8')
df = df.sort_values(by = "date", ascending = False)

df['arithmetic_return'] = (df['close'] / df['close'].shift(1)) - 1
df = df.dropna()

mean = df['arithmetic_return'].mean()
std = df['arithmetic_return'].std()
z5 = 1.65

norm_VaR = round((-mean + std * z5) * 10000, 2)
print(norm_VaR)

# python program to demonstrate parametric lognormal VaR

import pandas as pd
import numpy as np
import math

df = pd.read_csv('SPY.csv', index_col='date', sep=',', encoding='utf-8')
df = df.sort_values(by = "date", ascending = False)

df['geometric_return'] = np.log(df['close'] / df['close'].shift(1))
df = df.dropna()

mean = df['geometric_return'].mean()
std = df['geometric_return'].std()
z5 = 1.65

log_VaR = round(10000 * (1-math.exp(mean - std * z5)), 2)
print(log_VaR)
