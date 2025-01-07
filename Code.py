import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('generated_data.csv')

#Perform Kruskal-Wallis test
kruskal_stat, kruskal_p = stats.kruskal(
    data[data['Group'] == 'A']['Value'],
    data[data['Group'] == 'B']['Value'],
    data[data['Group'] == 'C']['Value']
)

# Perform ANOVA test
anova_stat, anova_p = stats.f_oneway(
    data[data['Group'] == 'A']['Value'],
    data[data['Group'] == 'B']['Value'],
    data[data['Group'] == 'C']['Value']
)

# Print the results
print("Kruskal-Wallis Test: Statistic = {:.4f}, p-value = {:.4f}".format(kruskal_stat, kruskal_p))
print("ANOVA Test: Statistic = {:.4f}, p-value = {:.4f}".format(anova_stat, anova_p))

# Set a color palette for better visualization
palette = sns.color_palette("Set2", n_colors=3)  # A pleasant color palette

# Visualize the results with improved coloring
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Boxplot for Kruskal-Wallis test comparison
sns.boxplot(x='Group', y='Value', data=data, ax=axes[0, 0], hue='Group', palette=palette, legend=False)
axes[0, 0].set_title("Kruskal-Wallis Test: Boxplot")
axes[0, 0].set_ylabel("Value")
axes[0, 0].set_xlabel("Group")

# Violin plot for Kruskal-Wallis test comparison
sns.violinplot(x='Group', y='Value', data=data, ax=axes[0, 1], hue='Group', palette=palette, legend=False)
axes[0, 1].set_title("Kruskal-Wallis Test: Violin Plot")
axes[0, 1].set_ylabel("Value")
axes[0, 1].set_xlabel("Group")

# Boxplot for ANOVA test comparison
sns.boxplot(x='Group', y='Value', data=data, ax=axes[1, 0], hue='Group', palette=palette, legend=False)
axes[1, 0].set_title("ANOVA Test: Boxplot")
axes[1, 0].set_ylabel("Value")
axes[1, 0].set_xlabel("Group")

# Violin plot for ANOVA test comparison
sns.violinplot(x='Group', y='Value', data=data, ax=axes[1, 1], hue='Group', palette=palette, legend=False)
axes[1, 1].set_title("ANOVA Test: Violin Plot")
axes[1, 1].set_ylabel("Value")
axes[1, 1].set_xlabel("Group")

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
