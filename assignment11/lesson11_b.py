import plotly.express as px
import plotly.data as pldata

# Load sample iris dataset as a DataFrame
df = pldata.iris(return_type='pandas')

# Create an interactive scatter plot
fig = px.scatter(
    df,
    x='sepal_length',
    y='petal_length',
    color='species',
    title="Iris Data, Sepal vs. Petal Length",
    hover_data=["petal_length"]
)

# Save the plot as an HTML file and open it in the browser
fig.write_html("iris.html", auto_open=True)
