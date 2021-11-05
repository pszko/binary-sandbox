# python program to demonstrate martingale returns

import pandas as pd
import numpy as np

portefeuille_l = []

for game in range(1000):
    print(game)
    wallet = 0
    y = 1

    for x in range(50):
        gamble = y * 25
        wallet = wallet - gamble
        z = np.random.choice(np.arange(0, 2), p=[0.5135, 0.4865])

        if z == 1:
            win = gamble * 2
            wallet = wallet + win
            y = 1
        else:
            y = y * 2
            y = min(y, 64)
    portefeuille_l.append(wallet)

portefeuille_df = pd.DataFrame(portefeuille_l, columns = ['Amount'])

# ---
# python program to plot martingale returns

import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Martingale Returns')

ax = sns.distplot(portefeuille_df['Amount'], hist = False, kde = True, rug = True,
             color = 'green',
             hist_kws={'edgecolor':'none'},
             kde_kws={'linewidth': 1})

maximum = portefeuille_df['Amount'].max()
maximum = "Maximum: " + str(maximum)

minimum = portefeuille_df['Amount'].min()
minimum = "Minimum: " + str(minimum)

q1 = portefeuille_df['Amount'].quantile(0.25)
q1 = "Quartile 1: " + str(q1)

q2 = portefeuille_df['Amount'].quantile(0.50)
q2 = "Quartile 2: " + str(q2)

q3 = portefeuille_df['Amount'].quantile(0.75)
q3 = "Quartile 3: " + str(q3)

mean = portefeuille_df['Amount'].mean()
mean = "Mean: " + str(mean)

ax.text(0.1, 0.90, maximum,
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='darkgreen', fontsize=10)

ax.text(0.1, 0.85, minimum,
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='darkgreen', fontsize=10)

ax.text(0.1, 0.80, q1,
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='darkgreen', fontsize=10)

ax.text(0.1, 0.75, q2,
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='darkgreen', fontsize=10)

ax.text(0.1, 0.70, q3,
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='darkgreen', fontsize=10)

ax.text(0.1, 0.65, mean,
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='darkgreen', fontsize=10)

ax = sns.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)

plt.savefig('martingale_returns.png')
plt.show()
