import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Generate random data
set1 = np.random.randint(0, 40, 24)
set2 = np.random.randint(0, 100, 24)

# Put into dataframe
df = pd.DataFrame({'set1': set1, 'set2': set2})
data = pd.melt(df)

# Plot
fig, ax = plt.subplots()
sns.swarmplot(data=data, x='variable', y='value', ax=ax)

# Now connect the dots
# Find idx0 and idx1 by inspecting the elements return from ax.get_children()
# ... or find a way to automate it
idx0 = 0
idx1 = 1
locs1 = ax.get_children()[idx0].get_offsets()
locs2 = ax.get_children()[idx1].get_offsets()
print(locs1, locs2)
for i in range(locs1.shape[0]):
    x = [locs1[i, 0], locs2[i, 0]]
    y = [locs1[i, 1], locs2[i, 1]]
    ax.plot(x, y, color='black', alpha=0.1)

plt.show()