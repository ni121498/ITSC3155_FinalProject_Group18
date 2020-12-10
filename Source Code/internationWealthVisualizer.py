import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('../Data_Sets/GDP.csv')

fig = go.Figure(data = go.Choropleth(
    locations = df['Country Code'],
    z = df['2019 [YR2019]'],
    text = df['Country Name'],
    colorscale= 'Blues',
    autocolorscale= False,
    reversescale= True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix= '$',
    colorbar_title='GDP<br>US$',
))

fig.update_layout(
    title_text='2019 Global GDP',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source= <a href="https://databank.worldbank.org/source/world-development-indicators#"> World Bank</a>',
        showarrow=False
    )
                   ]
)
fig.write_html('world.html', auto_open = True)