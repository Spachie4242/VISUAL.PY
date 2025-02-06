import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
months = ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019']
searches = [50, 80, 59, 56, 62]
direct = [39, 53, 42, 51, 51]
social_media = [70, 47, 90, 87, 92]

x = np.arange(len(months))  # X-axis positions
bar_width = 0.25

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the bars
ax.bar(x - bar_width, searches, bar_width, label='Searches', color='blue')
ax.bar(x, direct, bar_width, label='Direct', color='pink')
ax.bar(x + bar_width, social_media, bar_width, label='Social Media', color='orange')

# Adding labels, title, and legend
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Visitors (in thousands)', fontsize=12)
ax.set_title('Visitors by Web Traffic Sources', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.legend()

# Grid and layout adjustments
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the chart
plt.show()
