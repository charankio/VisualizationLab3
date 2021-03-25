import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

trace1 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='actual_mean_temp')
trace2 = go.Scatter(x=df['date'], y=df['actual_min_temp'], mode='lines', name='actual_min_temp')
trace3 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='actual_max_temp')
data = [trace1, trace2, trace3]

layout = go.Layout(title='Max & Min and Mean temperature of each month from 2014-2015', xaxis_title="Date",
                   yaxis_title="Temperature")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')
