import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd
import pathlib
from pathlib import Path
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
# get relative data folder


df_flat = pd.read_csv('Dashboard_file preprocessed df.csv')

CO2_df = df_flat.loc[df_flat['Series Name'] == 'CO2 emissions (kt)']
CO2_df2020 = CO2_df.loc[CO2_df['Year'] == 2016]
top5 = CO2_df2020.sort_values(by=['value'], ascending=False).head(5)
fig = px.bar(top5.sort_values(by=['value']), x='Country Name', y='value',
             labels={'value': 'CO2 emissions (kt)'}, title='CO2 emissions (kt) - Top 5 nations in Year 2016')
fig.update_xaxes(fixedrange=True)

# Below code defines the layout of the dashboard. It defines how the dashboard will appear as a web page.
app.layout = html.Div(children=[
    html.H1(children='Climate Change Dashboard', style={
        'textAlign': 'center'
    }),
    html.Div(children='''
      CO2 emissions (kt)''', style={
        'textAlign': 'center'
    }),
    html.Div([
        dcc.Graph(id='bar-chart', figure=fig)], style={'width': '80%', 'display': 'inline-block'})

])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
