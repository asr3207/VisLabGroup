import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../Datasets/Weather2014-15.csv')

data = [go.Heatmap(x=df['month'],
                   y=df['day'],
                   z=df['actual_max_temp'].values.tolist(),
                   colorscale='Jet')]

layout = go.Layout(title='Max temperatures', xaxis_title="Month", yaxis_title="Day of week")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Watherheatmap.html')