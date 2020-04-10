import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df2 = pd.read_csv('../Datasets/Olympic2016Rio.csv')

app = dash.Dash()

# Barchart
filtered_df = df1.nlargest(20, 'Total')
new_df = filtered_df.groupby(['NOC'])['Total'].sum().reset_index()
new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]

# Stacked barchart
new_df = df2.groupby(['NOC']).agg({'Total': 'sum', 'Bronze': 'sum',
'Silver': 'sum', 'Gold':'sum'}).reset_index()
new_df = new_df.sort_values(by=['Total'],
ascending=[False]).head(20).reset_index()
trace1 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold', marker={'color': '#FFD700'})
data_stackbarchart = [trace1, trace2, trace3]
#layout = go.Layout(title='Number of Medals', xaxis_title="Country", yaxis_title="Number of Medals", barmode='stack')

app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('2016 Olympic Rio Statistics', style={'textAlign': 'center'}),
    #html.Div('Testing', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Br(),

    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the number medals per country.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Most Medals', xaxis_title="Country", yaxis_title="Totals")
              }),

    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represent the type of metal earned by each country bronze, silver, and gold'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='Number of Medals', xaxis_title="Country", yaxis_title="Number of Medals", barmode='stack')
              })
              ])

if __name__ == '__main__':
    app.run_server()
