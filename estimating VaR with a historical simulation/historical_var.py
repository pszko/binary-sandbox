
# Python program to demonstrate historical VaR

import pandas as pd
import numpy as np

df = pd.read_csv('SPY.csv', index_col='date', sep=',', encoding='utf-8')
df = df.sort_values(by = "date", ascending = False)

df['arithmetic_return'] = (df['close'] / df['close'].shift(1)) - 1
df = df.dropna()

n = 1000
df = df.iloc[:n]

df = df.sort_values(by = 'arithmetic_return', ascending = True)

CI = 0.95
alpha = 1 - CI
thresh = round(alpha * n, 0)

VaR = df.iloc[[thresh], [6]].to_numpy()
print(VaR)

# ---

# Python program to plot historical VaR

import matplotlib.pyplot as plt
import seaborn as sns

data = df['arithmetic_return']
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('SPY returns')

ax = sns.distplot(data, hist = True, kde = True,
             color = 'darkgreen',
             hist_kws={'edgecolor':'none'},
             kde_kws={'linewidth': 1})

maximum = round(data.max(), 4)
maximum = "Maximum: " + str(maximum)

minimum = round(data.min(), 4)
minimum = "Minimum: " + str(minimum)

VaRx = round(float(VaR[0]),4)
VaRx = "Return: " + str(VaRx)

ax.text(0.05, 0.90, maximum,
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        fontsize=10)

ax.text(0.05, 0.85, minimum,
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        fontsize=10)

ax.text(0.05, 0.80, VaRx,
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        fontsize=10)

ax = sns.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)

plt.axvline(VaR, 0,0.8)

plt.xlabel("Arithmetic returns")
plt.ylabel("Density")

plt.savefig('SPY returns.png')
plt.show()
