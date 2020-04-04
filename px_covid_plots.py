import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/RadicalPrecursor/Covid-19-MA/master/by_location.csv')

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Day'], y=df['Suffolk'], 
                    mode='markers',
                    name='Suffolk County'))
fig.add_trace(go.Scatter(x=df['Day'], y=df['Middlesex'], 
                    mode='markers',
                    name='Middlesex County'))
fig.add_trace(go.Scatter(x=df['Day'], y=df['Norfolk'], 
                    mode='markers',
                    name='Norfolk County'))
fig.add_trace(go.Scatter(x=df['Day'], y=df['Essex'], 
                    mode='markers',
                    name='Essex County'))
'''
fig.update_layout(
    title="County Confirmed Cases",
    xaxis_title="Date, 2020",
    yaxis_title="COVID-19 Cases",
    )
fig.show()

fig = px.scatter(x=df['Day'], y=df['MA Total'], log_y=True)
fig.update_layout(
    title="Log Plot of Massachusetts Confirmed Cases",
    xaxis_title="Date, 2020",
    yaxis_title="COVID-19 Cases in MA",
    )
'''
fig.show()
