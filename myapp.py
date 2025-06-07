from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# Load gapminder data
df = px.data.gapminder()

# Initialize Dash app
app = Dash(__name__)

server = app.server

# List of unique countries
countries = df['country'].unique()

# Layout
app.layout = html.Div([
    html.H1("GDP per Capita Over Time"),
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic graph update
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP per Capita for {selected_country} Over Time"
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)