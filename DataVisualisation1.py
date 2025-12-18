import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# 1. Setup Data
data = {
    'Country': [
        'India', 'China', 'United States', 'Indonesia', 'Pakistan',
        'Nigeria', 'Brazil', 'Bangladesh', 'Russia', 'Ethiopia'
    ],
    'Population (millions)': [
        1464, 1416, 347, 286, 255,
        238, 213, 176, 144, 135
    ]
}

# 2. Process Data
df = pd.DataFrame(data)
df = df.sort_values(by='Population (millions)', ascending=True)

# 3. Create Visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Create a color gradient based on values
norm = plt.Normalize(df['Population (millions)'].min(), df['Population (millions)'].max())
colors = cm.viridis(norm(df['Population (millions)'])) # 'viridis' is great for readability

bars = ax.barh(df['Country'], df['Population (millions)'], color=colors, edgecolor='none')

# 4. Add Labels and Styling
for bar in bars:
    width = bar.get_width()
    ax.text(width + 10, bar.get_y() + bar.get_height()/2,
            f'{int(width):,}', va='center', fontsize=11, fontweight='bold')

# Clean up the chart area
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(False)

plt.title('Top 10 Most Populous Countries (Est. Dec 2025)', 
          fontsize=18, fontweight='bold', pad=25, loc='center')
plt.xlabel('Population (in Millions)', fontsize=12, labelpad=10)
plt.grid(axis='x', linestyle='--', alpha=0.4)

# 5. Display and Save
plt.tight_layout()

try:
    plt.savefig('top10_population_2025.png', dpi=300, bbox_inches='tight')
    print("Success: Chart saved as 'top10_population_2025.png'")
except Exception as e:
    print(f"Note: Could not save file due to: {e}")

plt.show()
