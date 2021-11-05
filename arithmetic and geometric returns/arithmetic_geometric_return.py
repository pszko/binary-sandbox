# # Python program to demonstrate arithmetic return - simple method
#
# P0 = 4    # Pt-1
# P1 = 5    # Pt
# D1 = 1    # Dt
#
# arithmetic_return = ((P1 + D1) / P0) - 1
#
# print(arithmetic_return)
#
# # Python program to demonstrate arithmetic return - with pandas
# import pandas as pd
#
# df = pd.read_csv('SPY.csv', index_col='date', sep=',', encoding='utf-8')
# df = df.sort_values(by = "date")
#
# df['arithmetic_return'] = (df['close'] / df['close'].shift(1)) - 1
#
# print(df.head())

# df['arithmetic_return_pct'] = (df['close'].pct_change(1))



# # Python program to demonstrate geometric return - with numpy
# import pandas as pd
# import numpy as np
#
# def geometric_return(iter):
#     x = np.array(iter)
#     return x.prod()**(1.0/len(x))
#
# df = pd.read_csv('SPY.csv', index_col='date', sep=',', encoding='utf-8')
# df = df.sort_values(by = "date")
#
# df['geometric_return'] = geometric_return(df['close'])
# print(df.head())


# # Python program to demonstrate geometric return - with numpy (overflow)
# import pandas as pd
# import numpy as np
#
# def geometric_return(iterable):
#     a = np.log(iterable)
#     return np.exp(a.mean())
#
# df = pd.read_csv('SPY.csv', index_col='date', sep=',', encoding='utf-8')
# df = df.sort_values(by = "date")
#
# df['geometric_return'] = geometric_return(df['close'])
# print(df.head())

# # Python program to demonstrate geometric return - with statistics
# import pandas as pd
# from statistics import geometric_mean
#
# df = pd.read_csv('SPY.csv', index_col='date', sep=',', encoding='utf-8')
# df = df.sort_values(by = "date")
#
# df['geometric_return'] = geometric_mean(df['close'])
# print(df.head())

# Python program to demonstrate geometric return - with numpy

import pandas as pd
import numpy as np

df = pd.read_csv('SPY.csv', index_col='date', sep=',', encoding='utf-8')
df = df.sort_values(by = "date")

df['arithmetic_return'] = (df['close'] / df['close'].shift(1)) - 1
df['geometric_return'] = np.log(df['close'] / df['close'].shift(1))

print(df.head(10))

df.to_csv('SPY_returns.csv')
