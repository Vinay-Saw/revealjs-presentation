import pandas as pd
import json

def parse_currency(value):
    if isinstance(value, str):
        return float(value.replace('$', '').replace(',', '').strip())
    return value

# Load data
try:
    df = pd.read_csv('Movie Revenue Data.csv')
except Exception as e:
    print(f"Error loading CSV: {e}")
    exit(1)

# Clean data
df['Production Budget'] = df['Production Budget ($)'].apply(parse_currency)
df['Worldwide Gross'] = df['Worldwide Gross ($)'].apply(parse_currency)
df['Domestic Gross'] = df['Domestic Gross ($)'].apply(parse_currency)
df['Release Date'] = pd.to_datetime(df['Release Date'])
df['Year'] = df['Release Date'].dt.year

# Analysis
# 1. Total Revenue per Year
yearly_revenue = df.groupby('Year')[['Worldwide Gross', 'Production Budget']].sum().reset_index()
yearly_revenue = yearly_revenue.sort_values('Year')

# 2. Top 5 Movies by Worldwide Gross
top_movies = df.sort_values('Worldwide Gross', ascending=False).head(5)[['Movie Title', 'Worldwide Gross', 'Year']]

# 3. ROI (Return on Investment)
df['ROI'] = (df['Worldwide Gross'] - df['Production Budget']) / df['Production Budget'] * 100
top_roi = df[df['Production Budget'] > 1000000].sort_values('ROI', ascending=False).head(5)[['Movie Title', 'ROI', 'Year']]

# Prepare data for export
data = {
    'yearly_revenue': yearly_revenue.to_dict(orient='records'),
    'top_movies': top_movies.to_dict(orient='records'),
    'top_roi': top_roi.to_dict(orient='records'),
    'total_movies': len(df),
    'total_gross': df['Worldwide Gross'].sum(),
    'average_budget': df['Production Budget'].mean()
}

# Save to JS file
with open('data.js', 'w') as f:
    f.write(f"const movieData = {json.dumps(data, indent=2)};")

print("Data analysis complete. Saved to data.js")
