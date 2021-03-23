import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating Gold column
df['Gold'] = df['Total'] - df['Silver'] - df['Bronze']

# Creating sum of medals by Country Column
new_df = df.groupby(['NOC']).agg(
    {'Total': 'sum', 'Bronze': 'sum', 'Silver': 'sum', 'Gold': 'sum'}).reset_index()

# Sorting values and select 20 first value
new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20).reset_index()

# Preparing data
trace1 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold', marker={'color': '#FFD700'})
trace2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze', marker={'color': '#CD7F32'})
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Medals of Olympic 2016 of 20 first top countries', xaxis_title="Country",
                   yaxis_title="Medals Won", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')
