# %%
import pandas as pd


import matplotlib.pyplot as plt

# %%
print("All packages imported successfully!")

# %%
print(f"Pandas version: {pd.__version__}")

# %% [markdown]
# ### Working with Jupyter Notebook

# %% [markdown]
# #### Data Loading

# %%
df = pd.read_csv('UNRATE.csv')

# %%
print(df.columns)

# %%
df['observation_date'] = pd.to_datetime(df['observation_date'])

# %%
print("Dataset shape:", df.shape)

# %%
print("\nFirst 5 rows:")
df.head()

# %%
print("Data types:")
print(df.dtypes)
print("\nBasic statistics:")
df['UNRATE'].describe()

# %%
max_unrate = df['UNRATE'].max()
max_date = df[df['UNRATE'] == max_unrate]['observation_date'].values[0]
print(f"Max unemployment rate: {max_unrate}% on {max_date}")


# %% [markdown]
# ### Part 5: Business Data Analysis

# %%
df = df.rename(columns={'observation_date': 'DATE'})

# %%
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)

# %% [markdown]
# #### Statistical Analysis

# %%
#overall employment rate
print("\nBasic statistics:")
df['UNRATE'].describe()

# %%
#Find minimum and maximum unemployment rates with their dates
# Max unemployment rate
max_row = df.loc[df['UNRATE'].idxmax()]
max_rate = max_row['UNRATE']
max_date = max_row['DATE'].strftime('%Y-%m-%d')

# Min unemployment rate
min_row = df.loc[df['UNRATE'].idxmin()]
min_rate = min_row['UNRATE']
min_date = min_row['DATE'].strftime('%Y-%m-%d')

# Display results
print(f"Maximum unemployment rate: {max_rate}% on {max_date}")
print(f"Minimum unemployment rate: {min_rate}% on {min_date}")


# %%
#Calculate unemployment statistics by decade (1950s, 1960s, etc.)
df['Decade'] = (df['DATE'].dt.year // 10) * 10
decade_avg = df.groupby('Decade')['UNRATE'].mean()

# Create visualizations
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Time series plot
ax1.plot(df['DATE'], df['UNRATE'])
ax1.set_title('US Unemployment Rate Over Time')
ax1.set_xlabel('Year')
ax1.set_ylabel('Unemployment Rate (%)')

# Decade averages
decade_avg.plot(kind='bar', ax=ax2)
ax2.set_title('Average Unemployment Rate by Decade')
ax2.set_xlabel('Decade')
ax2.set_ylabel('Average Unemployment Rate (%)')
plt.tight_layout()
plt.savefig('unemployment_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# %%
# Extract the year from the DATE column
df['Year'] = df['DATE'].dt.year

# Group by year and compute average unemployment rate
yearly_avg = df.groupby('Year')['UNRATE'].mean()

# Find the year with the highest average
max_year = yearly_avg.idxmax()
max_rate = yearly_avg.max()

# Display result
print(f"The year with the highest average unemployment rate is {int(max_year)} with an average rate of {max_rate:.2f}%")


# %%
# Create the plot for average unemployment rate over the year
plt.figure(figsize=(12, 6))
plt.plot(yearly_avg.index, yearly_avg.values, marker='o', linestyle='-', color='purple')
plt.title('Average Unemployment Rate by Year')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()


plt.savefig('average_unemployment_by_year.png', dpi=300, bbox_inches='tight')
plt.show()

# %%
avg_2015 = df[df['Year'] == 2015]['UNRATE'].mean()
avg_2025 = df[df['Year'] == 2025]['UNRATE'].mean()

# %%
print(f"Average unemployment rate in 2015: {avg_2015:.2f}%")
print(f"Average unemployment rate in 2025: {avg_2025:.2f}%")

# %%
# Calculate standard deviation of unemployment rates by decade
decade_std = df.groupby('Decade')['UNRATE'].std()

# Display the result
print(decade_std)


# %%



