import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Preparing data, we got average min temp and average max temp from weather2014-15.csv dataset, the text define the date.
# the mode is red dotted line with date average temp sort by time
data = [
    go.Scatter(x=df['average_min_temp'],
               y=df['average_max_temp'],
               text=df['date'],
               mode='markers', marker=dict(size=8,color='red'))
]

# Preparing layout
layout = go.Layout(title=' the average min and max temperature of each month in weather statistics', xaxis_title="Average Min Temp",
                   yaxis_title="Average Max Temp", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')