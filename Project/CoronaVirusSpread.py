import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('CoronaVirusCasesUpdated.csv')
df2 = pd.read_csv('NC-Coronavirus - Sheet1.csv')
df3 = pd.read_csv('CoronaVirusCasesWeekly.csv')
df2['Date'] = pd.to_datetime(df2['Date'])

app = dash.Dash()

# heat map confirmed cases / population
fig = go.Figure(data=go.Choropleth(
    locations=df['Code'],
    z=df['CasePop'].astype(float),
    locationmode='USA-states',
    colorscale='bupu',
    colorbar_title="% of population with corona virus",
))
fig.update_layout(
    title_text='Percentage of population confirmed corona cases',
    geo_scope='usa',
)

# heat map of deaths across country
fig2 = go.Figure(data=go.Choropleth(
    locations=df['Code'],
    z=df['Deaths'].astype(float),
    locationmode='USA-states',
    colorscale='reds',
    colorbar_title='# of deaths'
))
fig2.update_layout(
    title_text='Number of deaths across the country',
    geo_scope='usa',
)

# heat map for number of recoverd
fig3 = go.Figure(data=go.Choropleth(
    locations=df['Code'],
    z=df['Recovered'].astype(float),
    locationmode='USA-states',
    colorscale='greens',
    colorbar_title='# of recovered'
))
fig3.update_layout(
    title_text='Number of recoverd cases across the country',
    geo_scope='usa'
)

# Line chart for cumulative number of cases
LineChartData = [go.Scatter(x=df2['Date'], y=df2['Cumulative'], mode='lines',
                            name='Cumulative number of cases per day in North Carolina')]

# animated map of number of cases
figA = go.Figure(data=go.Choropleth(
    locations=df3['Code'],
    z=df3['March1'].astype(float),
    locationmode='USA-states',
    colorscale='bupu',
    colorbar_title="Confirmed Cases of Covid-19",
    zauto=False,
    zmin=0,
    zmax=300000
),
    frames=[go.Frame(data=go.Choropleth(z=df3['March1'].astype(float), text="Week 1 of March")),
            go.Frame(data=go.Choropleth(z=df3['March2'].astype(float), text="Week 2 of March")),
            go.Frame(data=go.Choropleth(z=df3['March3'].astype(float), text="Week 3 of March")),
            go.Frame(data=go.Choropleth(z=df3['March4'].astype(float), text="Week 4 of March")),
            go.Frame(data=go.Choropleth(z=df3['April1'].astype(float), text="Week 1 of April")),
            go.Frame(data=go.Choropleth(z=df3['April2'].astype(float), text="Week 2 of April")),
            go.Frame(data=go.Choropleth(z=df3['April3'].astype(float), text="Week 3 of April")),
            go.Frame(data=go.Choropleth(z=df3['April4'].astype(float), text="Week 4 of April")),
            go.Frame(data=go.Choropleth(z=df3['May1'].astype(float), text="Week 1 of May")),
            ]

)
figA.update_layout(
    title_text='Confirmed Coronavirus Cases',
    geo_scope='usa',
    updatemenus=[dict(
        type="buttons",
        buttons=[dict(label="Play",
                      method="animate",
                      args=[None])])],
)

app.layout = html.Div(children=[
    html.H1(children='Visualization of the Corona virus',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.H3('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.H3('The state of Coronavirus COVID-19 Global Cases as of 4/19/2020', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(), html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Percentage of population infected', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represent the Corona Virus confirmed cases divided by the total population of the state'),
    dcc.Graph(id='graph',
              figure=fig
              ),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Death map', style={'color': '#df1e56'}), html.Div(
        'Heat map of the number of deaths across the country'),
    dcc.Graph(id='graph2',
              figure=fig2
              ),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Recovered cases', style={'color': '#df1e56'}), html.Div(
        'Heat map of the number of recoverd cases across the country'),
    html.Div(
        'Data skewed due to large number of states not having reported recovered cases'
    ),
    dcc.Graph(id='graph3',
              figure=fig3
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the Corona Virus confirmed cases of all reported cases in the given period.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': LineChartData,
                  'layout': go.Layout(
                      title='Cumulative number of cases in North Carolina per day 03/01/2020 - 04/18/2020',
                      xaxis_title="Date", yaxis_title="Number of Cases")
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Animated Chart', style={'color': '#df1e56'}),
    html.Div('This animated chart shows the number of cases updated once a week from March 1st to May 1st'),
    dcc.Graph(id='graph6',
              figure=figA
              ),
])

if __name__ == '__main__':
    app.run_server()

# Dashboard
# This map % total population of confirmed cases
# Death map
# recovered map -- disclaimer of not all states had data for it
# Cumulative number of cases in North Carolina per day
# (ADD) Number of new cases in North Carolina per day
# (ADD) timelaps of the spread of the cases in interactive graph
