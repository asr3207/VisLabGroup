import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')

new_df = df.groupby(['month']).agg({'actual_max_temp': 'max', 'actual_min_temp': 'min', 'actual_mean_temp': 'mean'}).reset_index()

trace1 = go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='Max')
trace2 = go.Scatter(x=new_df['month'], y=new_df['actual_min_temp'], mode='lines', name='Min')
trace3 = go.Scatter(x=new_df['month'], y=new_df['actual_mean_temp'], mode='lines', name='Mean')
data = [trace1, trace2, trace3]

layout = go.Layout(title="Max, Min, and Mean temperatures", xaxis_title="Month", yaxis_title="Temps")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='WeatherMultiLineChart.html')