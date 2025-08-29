import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt

# SCRAPING
print("Phase 1: Scraping data from Wikipedia...")
URL = "https://en.wikipedia.org/wiki/List_of_largest_cities"
HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
})

webpage = requests.get(URL, headers=HEADERS)
tables = pd.read_html(StringIO(webpage.text))
df = tables[1]
df.to_csv('largest_cities.csv', index=False)

print("Data successfully scraped and saved to largest_cities.csv!")

# VISUALIZATION
print("\nPhase 2: Creating data visualization...")

df_cities = pd.read_csv('largest_cities.csv')

# Data_Cleaning
# We will work with a copy to keep the original data safe.

df_plot = df_cities.copy()

# Select the population column
population_column = df_plot.columns[2]

# Remove any rows that have non-numeric data in the population column
df_plot = df_plot[pd.to_numeric(df_plot[population_column], errors='coerce').notna()]

# Clean the population column
df_plot[population_column] = df_plot[population_column].str.replace(',', '', regex=False).astype(int)

# Sort the data by population and get the top 10 cities.
df_top10 = df_plot.sort_values(by=population_column, ascending=False).head(10)

# Creating Bar Chart
plt.figure(figsize=(12, 8))
plt.bar(df_top10['City[a]'], df_top10[population_column], color='skyblue')

plt.xlabel('City', fontsize=12)
plt.ylabel('Population (in tens of millions)', fontsize=12)
plt.title('Top 10 Most Populous Cities (UN 2018 Estimates)', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.tight_layout() 

# Save the chart to an image file
plt.savefig('top_10_cities_population.png')

print("Chart successfully saved as top_10_cities_population.png!")