import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read the CSV file
data = pd.read_csv('generated_data.csv')

# Step 2: Perform parametric (ANOVA) test
anova_stat, anova_p = stats.f_oneway(
    data[data['Group'] == 'A']['Value'],
    data[data['Group'] == 'B']['Value'],
    data[data['Group'] == 'C']['Value']
)

# Step 3: Perform non-parametric (Kruskal-Wallis) test
kruskal_stat, kruskal_p = stats.kruskal(
    data[data['Group'] == 'A']['Value'],
    data[data['Group'] == 'B']['Value'],
    data[data['Group'] == 'C']['Value']
)

# Step 4 Print the test results
print(f"ANOVA Test: Statistic = {anova_stat:.4f}, p-value = {anova_p:.4f}")
print(f"Kruskal-Wallis Test: Statistic = {kruskal_stat:.4f}, p-value = {kruskal_p:.4f}")

# Step 5: Visualise the data and results
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
# Set a color palette for better visualization
palette = sns.color_palette("Set2", n_colors=3)  # A pleasant color palette
# Boxplot for raw values
sns.boxplot(x='Group', y='Value', data=data, ax=axes[0, 0], hue='Group', palette=palette, legend=False)
axes[0, 0].set_title("Boxplot of Raw Values")
axes[0, 0].set_xlabel("Group")
axes[0, 0].set_ylabel("Value")

# Violin plot for raw values
sns.violinplot(x='Group', y='Value', data=data, ax=axes[0, 1], hue='Group', palette=palette, legend=False)
axes[0, 1].set_title("Violin Plot of Raw Values")
axes[0, 1].set_xlabel("Group")
axes[0, 1].set_ylabel("Value")

# Boxplot for ranks (Kruskal-Wallis test)
data['Rank'] = stats.rankdata(data['Value'])
sns.boxplot(x='Group', y='Rank', data=data, ax=axes[1, 0], hue='Group', palette=palette, legend=False)
axes[1, 0].set_title("Boxplot of Ranks (Kruskal-Wallis)")
axes[1, 0].set_xlabel("Group")
axes[1, 0].set_ylabel("Rank")

# Violin plot for ranks (Kruskal-Wallis test)
sns.violinplot(x='Group', y='Rank', data=data, ax=axes[1, 1], hue='Group', palette=palette, legend=False)
axes[1, 1].set_title("Violin Plot of Ranks (Kruskal-Wallis)")
axes[1, 1].set_xlabel("Group")
axes[1, 1].set_ylabel("Rank")

# Adjust layout and display the plots
plt.tight_layout()
plt.show()

# Step 6: Summarise the findings
print("\nSummary:")
if anova_p < 0.05:
    print("ANOVA indicates a significant difference between groups.")
else:
    print("ANOVA does not indicate a significant difference between groups.")

if kruskal_p < 0.05:
    print("Kruskal-Wallis indicates a significant difference between groups.")
else:
    print("Kruskal-Wallis does not indicate a significant difference between groups.")
