import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Filtering US Cases
filtered_df = df.nlargest(20, 'Total')

# Removing empty spaces from State column to avoid errors
#filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by State Column
new_df = filtered_df.groupby(['NOC'])['Total'].sum().reset_index()

# Sorting values and select first 20 states
new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data
data = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]

# Preparing layout
layout = go.Layout(title='Most Medals', xaxis_title="Country",
                   yaxis_title="Totals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Olympicbarchart.html')