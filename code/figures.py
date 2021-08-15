
# importing package
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('seaborn')
# create data
df = pd.DataFrame([['Expanded', 140, 92, 61], ['Generated', 327, 216, 148]],
                  columns=['Results', 'Misplaced', 'Manhattan','new_method'])
# view data
ax = df.plot(x='Results',
        kind='bar',
        stacked=False,
        title='Results')

plt.show()
