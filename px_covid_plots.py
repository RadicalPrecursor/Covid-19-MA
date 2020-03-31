import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/RadicalPrecursor/RadicalPrecursor.github.io/master/by_location.csv')

fig = px.scatter(x=df['Day'], y=df['Suffolk'])
fig.update_layout(
    title="Suffolk County Confirmed Cases",
    xaxis_title="Date, 2020",
    yaxis_title="COVID-19 Cases in Suffolk County",
    )
fig.show()

fig = px.scatter(x=df['Day'], y=df['MA Total'], log_y=True)
fig.update_layout(
    title="Log Plot of Massachusetts Confirmed Cases",
    xaxis_title="Date, 2020",
    yaxis_title="COVID-19 Cases in MA",
    )
fig.show()
