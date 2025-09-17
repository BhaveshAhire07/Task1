import seaborn as sns
import matplotlib.pyplot as plt

# Age data
age_categories = ['0-20 years', '21-64 years', '65+ years']
age_populations = [512, 807, 98]  # in millions
age_colors = ['#FFC107', '#2196F3', '#F44336']

# Set style
sns.set_style("whitegrid")
plt.figure(figsize=(8, 6))
sns.barplot(x=age_categories, y=age_populations, hue=age_categories, palette=age_colors, legend=False)
plt.title("India's Population Distribution by Age in 2022")
plt.xlabel('Age Groups')
plt.ylabel('Population (Millions)')
plt.xticks(rotation=45)
for i, v in enumerate(age_populations):
    plt.text(i, v + 10, f'{v} Mn', ha='center', va='bottom')
plt.figtext(0.5, 0.9, 'Total: 1.42 billion | Median Age: 28 years', ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()