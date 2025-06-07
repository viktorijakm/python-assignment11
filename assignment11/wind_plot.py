import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load the wind dataset
df = pldata.wind(return_type='pandas')

# Print first and last 10 rows
print("First 10 rows:\n", df.head(10))
print("\nLast 10 rows:\n", df.tail(10))

# Clean the 'strength' column
# Convert values like '0-1' to average (e.g., (0+1)/2 = 0.5)
def parse_strength(val):
    if isinstance(val, str):
        if '-' in val:
            low, high = val.split('-')
            return (float(low) + float(high)) / 2
        elif '+' in val:
            return float(val.replace('+', '')) + 0.5
        else:
            return float(val)
    return val

df['strength'] = df['strength'].apply(parse_strength)

# Create interactive scatter plot
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title="Wind Strength vs Frequency by Direction",
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'},
    hover_data=['direction']
)

# Save and load HTML file
fig.write_html("wind.html")
print("✅ Plot saved to wind.html")
