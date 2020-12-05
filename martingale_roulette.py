import pandas as pd
import numpy as np


# ---Martingale


portefeuille_l = []

for game in range(1000000000):
    wallet = 0
    y = 1

    for x in range(15):
        gamble = y * 25
        wallet = wallet - gamble
        z = np.random.choice(np.arange(0, 2), p=[0.5135, 0.4865])

        if z == 1:
            win = gamble * 2
            wallet = wallet + win
            y = 1
        else:
            loss = gamble
            y = y * 2
            y = min(y, 64)
    portefeuille_l.append(wallet)

portefeuille_df = pd.DataFrame(portefeuille_l, columns = ['Amount'])

print(portefeuille_df)

# Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Density Plot and Histogram of all arrival delays
sns.distplot(portefeuille_df['Amount'], hist = False, kde = True, rug = True,
             color = 'darkgreen',
             hist_kws={'edgecolor':'none'},
             kde_kws={'linewidth': 1})

sns.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)

plt.title('Martingale Returns')
plt.show()
# # matplotlib histogram
# plt.hist(flights['arr_delay'], color = 'blue', edgecolor = 'black',
#          bins = int(180/5))
#
# # seaborn histogram
# sns.distplot(flights['arr_delay'], hist=True, kde=False,
#              bins=int(180/5), color = 'blue',
#              hist_kws={'edgecolor':'black'})
# # Add labels
# plt.title('Histogram of Arrival Delays')
# plt.xlabel('Delay (min)')
# plt.ylabel('Flights')



# seq = [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584]
#
# # print(seq[7])
#
#
#
# wallet = 0
# y = 0
# for x in range(10):
#     # print("wallet", wallet)
#     # print("y", y)
#     z = np.random.choice(np.arange(0, 2), p=[0.5135, 0.4865])
#     # print('z', z)
#     if z == 1:
#         wallet =+ seq[y] * 25
#         # y =-1
#         # y = max(y, 0)
#
#     else:
#         wallet =- seq[y] * 25
#         y =+ 1
#         if wallet < -200:
#             print("LOSER!!!")
#             break
# if wallet > 0:
#     print("Winner Winner Chicken Dinner")
#
# print("wallet", wallet)
