import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')

new_df = df.groupby(['month']).agg({'actual_max_temp': 'max'}).reset_index()

data = [go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='MaxTemp')]

layout = go.Layout(title='Max temperatures for each month of 2014', xaxis_title="Month", yaxis_title="Max Temps")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='WeatherLineChart.html')